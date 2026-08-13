from __future__ import annotations

import argparse
import base64
import json
import os
import statistics
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any


API_BASE = "https://openrouter.ai/api/v1"
MODEL_CANDIDATES = {
    "Laguna XS 2.1": "poolside/laguna-xs-2.1:free",
    "Laguna M.1": None,
    "North Mini Code": "cohere/north-mini-code:free",
}
VISION_CANDIDATES = [
    "google/gemma-4-26b-a4b-it:free",
    "google/gemma-4-31b-it:free",
    "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
    "nvidia/nemotron-nano-12b-v2-vl:free",
]
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Return current weather for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"},
                    "units": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["city", "units"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Evaluate a basic arithmetic expression.",
            "parameters": {
                "type": "object",
                "properties": {"expression": {"type": "string"}},
                "required": ["expression"],
                "additionalProperties": False,
            },
        },
    },
]
PROMPTS = [
    {
        "id": "plan",
        "messages": [
            {
                "role": "user",
                "content": (
                    "Create a concise implementation plan for adding a health-check endpoint "
                    "to a Python FastAPI service. Include validation and rollback. Do not use tools."
                ),
            }
        ],
        "tools": None,
    },
    {
        "id": "single_tool",
        "messages": [
            {
                "role": "user",
                "content": (
                    "Use the available tool to get Moscow weather in celsius. "
                    "Do not guess and do not answer without a tool call."
                ),
            }
        ],
        "tools": TOOLS,
        "expected_tool": "get_weather",
        "expected_arguments": {"city": "Moscow", "units": "celsius"},
    },
    {
        "id": "tool_choice",
        "messages": [
            {
                "role": "user",
                "content": "Use the correct available tool to calculate (37 * 19) + 8.",
            }
        ],
        "tools": TOOLS,
        "expected_tool": "calculator",
    },
]

# A deterministic 1x1 red PNG used only to verify that the vision route can inspect an image.
RED_PNG = base64.b64encode(
    base64.b64decode(
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Y9Zl2sAAAAASUVORK5CYII="
    )
).decode("ascii")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def safe_error(value: Any, api_key: str) -> str:
    text = str(value)
    if api_key:
        text = text.replace(api_key, "[REDACTED]")
    return text[:2000]


def api_request(
    path: str, api_key: str, payload: dict[str, Any] | None = None
) -> dict[str, Any]:
    headers = {"Accept": "application/json"}
    data = None
    method = "GET"
    if payload is not None:
        method = "POST"
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
        headers["Authorization"] = f"Bearer {api_key}"

    request = urllib.request.Request(
        f"{API_BASE}{path}", data=data, headers=headers, method=method
    )
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            body = json.load(response)
            return {
                "ok": True,
                "status": response.status,
                "latency_ms": round((time.perf_counter() - started) * 1000, 1),
                "body": body,
            }
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            body: Any = json.loads(raw)
        except json.JSONDecodeError:
            body = raw
        return {
            "ok": False,
            "status": exc.code,
            "latency_ms": round((time.perf_counter() - started) * 1000, 1),
            "error": safe_error(body, api_key),
        }
    except Exception as exc:
        return {
            "ok": False,
            "status": None,
            "latency_ms": round((time.perf_counter() - started) * 1000, 1),
            "error": safe_error(exc, api_key),
        }


def discover_models(api_key: str) -> tuple[list[dict[str, Any]], dict[str, str | None]]:
    result = api_request("/models", api_key)
    if not result["ok"]:
        raise RuntimeError(f"Model discovery failed: {result}")
    models = result["body"]["data"]
    free = [
        model
        for model in models
        if str((model.get("pricing") or {}).get("prompt")) == "0"
        and str((model.get("pricing") or {}).get("completion")) == "0"
    ]
    ids = {model["id"] for model in free}
    resolved = dict(MODEL_CANDIDATES)

    # Resolve Laguna M.1 only on a conservative exact-name/slug match.
    laguna_matches = [
        model["id"]
        for model in free
        if "laguna" in model["id"].lower()
        and any(token in model["id"].lower() for token in ("m-1", "m.1", "m1"))
    ]
    resolved["Laguna M.1"] = laguna_matches[0] if len(laguna_matches) == 1 else None
    for name, model_id in list(resolved.items()):
        if model_id not in ids:
            resolved[name] = None
    return free, resolved


def extract_answer(result: dict[str, Any]) -> dict[str, Any]:
    if not result["ok"]:
        return result
    choice = result["body"].get("choices", [{}])[0]
    message = choice.get("message") or {}
    return {
        "ok": True,
        "status": result["status"],
        "latency_ms": result["latency_ms"],
        "finish_reason": choice.get("finish_reason"),
        "content": message.get("content"),
        "tool_calls": message.get("tool_calls") or [],
        "usage": result["body"].get("usage"),
    }


def score_tool(prompt: dict[str, Any], answer: dict[str, Any]) -> dict[str, Any]:
    if not prompt.get("expected_tool"):
        return {"applicable": False}
    calls = answer.get("tool_calls") or []
    if not calls:
        return {"applicable": True, "success": False, "reason": "no tool call"}
    function = calls[0].get("function") or {}
    name_ok = function.get("name") == prompt["expected_tool"]
    try:
        arguments = json.loads(function.get("arguments") or "{}")
        valid_json = True
    except json.JSONDecodeError:
        arguments = {}
        valid_json = False
    expected = prompt.get("expected_arguments") or {}
    args_ok = all(
        str(arguments.get(key, "")).lower() == str(value).lower()
        for key, value in expected.items()
    )
    return {
        "applicable": True,
        "success": name_ok and valid_json and args_ok,
        "name_ok": name_ok,
        "arguments_json_ok": valid_json,
        "expected_arguments_ok": args_ok,
    }


def score_plan(content: str | None) -> dict[str, Any]:
    text = (content or "").lower()
    checks = {
        "implementation_steps": any(word in text for word in ("implement", "endpoint", "route")),
        "validation": any(word in text for word in ("test", "validate", "verify")),
        "rollback": "rollback" in text or "revert" in text,
        "concise_structure": 20 <= len(text.split()) <= 350,
    }
    return {"score": sum(checks.values()), "max": len(checks), "checks": checks}


def run_model(model_id: str, api_key: str, repeats: int) -> list[dict[str, Any]]:
    runs = []
    consecutive_429 = 0
    for repeat in range(repeats):
        for prompt in PROMPTS:
            payload: dict[str, Any] = {
                "model": model_id,
                "messages": prompt["messages"],
                "temperature": 0,
                "max_tokens": 500,
            }
            if prompt["tools"]:
                payload["tools"] = prompt["tools"]
                payload["tool_choice"] = "auto"
            answer = extract_answer(api_request("/chat/completions", api_key, payload))
            record = {
                "repeat": repeat + 1,
                "prompt_id": prompt["id"],
                **answer,
                "tool_score": score_tool(prompt, answer),
            }
            if prompt["id"] == "plan" and answer.get("ok"):
                record["plan_score"] = score_plan(answer.get("content"))
            runs.append(record)
            consecutive_429 = consecutive_429 + 1 if answer.get("status") == 429 else 0
            if consecutive_429 >= 2:
                return runs
    return runs


def run_vision(model_id: str, api_key: str) -> dict[str, Any]:
    payload = {
        "model": model_id,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What is the dominant color? Answer with one color word."},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{RED_PNG}"},
                    },
                ],
            }
        ],
        "temperature": 0,
        "max_tokens": 20,
    }
    answer = extract_answer(api_request("/chat/completions", api_key, payload))
    content = str(answer.get("content") or "").lower()
    answer["vision_success"] = answer.get("ok", False) and "red" in content
    return answer


def summarize_model(runs: list[dict[str, Any]]) -> dict[str, Any]:
    successful = [run for run in runs if run.get("ok")]
    latencies = [run["latency_ms"] for run in successful]
    tool_runs = [run for run in runs if run["tool_score"].get("applicable")]
    plan_scores = [run["plan_score"]["score"] for run in runs if "plan_score" in run]
    return {
        "requests": len(runs),
        "successes": len(successful),
        "tool_successes": sum(run["tool_score"].get("success", False) for run in tool_runs),
        "tool_attempts": len(tool_runs),
        "median_latency_ms": round(statistics.median(latencies), 1) if latencies else None,
        "mean_plan_score": round(statistics.mean(plan_scores), 2) if plan_scores else None,
        "http_429": sum(run.get("status") == 429 for run in runs),
        "http_5xx": sum(isinstance(run.get("status"), int) and run["status"] >= 500 for run in runs),
    }


def choose_routes(summary: dict[str, dict[str, Any]], vision: dict[str, Any]) -> dict[str, Any]:
    eligible = [
        (model, data)
        for model, data in summary.items()
        if data["successes"] > 0 and data["http_429"] == 0 and data["http_5xx"] == 0
    ]
    ranked = sorted(
        eligible,
        key=lambda item: (
            -(item[1]["tool_successes"] / max(item[1]["tool_attempts"], 1)),
            -(item[1]["mean_plan_score"] or 0),
            item[1]["median_latency_ms"] or float("inf"),
        ),
    )
    vision_ranked = sorted(
        (
            (model, result)
            for model, result in vision.items()
            if result.get("vision_success")
        ),
        key=lambda item: item[1].get("latency_ms") or float("inf"),
    )
    return {
        "default": ranked[0][0] if ranked else None,
        "fallback": ranked[1][0] if len(ranked) > 1 else None,
        "vision": vision_ranked[0][0] if vision_ranked else None,
        "rule": "tool success rate, then plan score, then median latency; zero 429/5xx required",
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        f"# OpenRouter benchmark — {report['date']}",
        "",
        "| Model | Requests | Success | Tool use | Median latency | Plan | 429 | 5xx |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for model, data in report["summary"].items():
        lines.append(
            f"| {model} | {data['requests']} | {data['successes']} | "
            f"{data['tool_successes']}/{data['tool_attempts']} | "
            f"{data['median_latency_ms'] or '-'} ms | {data['mean_plan_score'] or '-'}/4 | "
            f"{data['http_429']} | {data['http_5xx']} |"
        )
    lines.extend(["", "## Unavailable candidates", ""])
    lines.extend(f"- {name}" for name in report["unavailable"])
    lines.extend(["", "## Vision", "", "| Model | Success | Latency | HTTP |", "|---|---:|---:|---:|"])
    for model, result in report["vision"].items():
        lines.append(
            f"| {model} | {result.get('vision_success', False)} | "
            f"{result.get('latency_ms', '-')} ms | {result.get('status', '-')} |"
        )
    routes = report["routes"]
    lines.extend(
        [
            "",
            "## Selection",
            "",
            f"- Default: {routes['default'] or 'not selected'}",
            f"- Fallback: {routes['fallback'] or 'not selected'}",
            f"- Vision route: {routes['vision'] or 'not selected'}",
            f"- Rule: {routes['rule']}",
            "",
            "Automated plan scores are rubric checks, not a human semantic evaluation.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repeats", type=int, default=2)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    api_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not api_key:
        raise SystemExit("OPENROUTER_API_KEY is not set")

    free_models, resolved = discover_models(api_key)
    stamp = date.today().isoformat()
    free_path = args.output_dir / f"openrouter_free_{stamp}.txt"
    json_path = args.output_dir / f"openrouter_benchmark_{stamp}.json"
    md_path = args.output_dir / f"openrouter_benchmark_{stamp}.md"
    free_rows = sorted(model["id"] for model in free_models)
    free_path.write_text(
        f"Checked: {stamp}\n" + "\n".join(free_rows) + "\n", encoding="utf-8"
    )

    raw: dict[str, list[dict[str, Any]]] = {}
    unavailable = []
    for name, model_id in resolved.items():
        if model_id is None:
            unavailable.append(name)
            continue
        raw[model_id] = run_model(model_id, api_key, args.repeats)

    free_ids = {model["id"] for model in free_models}
    vision = {
        model_id: run_vision(model_id, api_key)
        for model_id in VISION_CANDIDATES
        if model_id in free_ids
    }
    summary = {model: summarize_model(runs) for model, runs in raw.items()}
    report = {
        "date": stamp,
        "generated_at": utc_now(),
        "resolved_candidates": resolved,
        "unavailable": unavailable,
        "prompts": PROMPTS,
        "raw_results": raw,
        "summary": summary,
        "vision": vision,
    }
    report["routes"] = choose_routes(summary, vision)
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(render_markdown(report), encoding="utf-8")
    print(json.dumps({"outputs": [str(free_path), str(json_path), str(md_path)], "routes": report["routes"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
