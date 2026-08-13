# Local AI Agent Integration Lab

A reproducible engineering case study: evaluate local and hosted language
models, connect a voice AI client to a loopback-only gateway, and verify the
result with security checks, automated tests, benchmarks, and operator
documentation.

```text
Open-LLM-VTuber
       |
       | OpenAI-compatible chat requests
       v
Local Agent Gateway (127.0.0.1:8642)
       |
       | authenticated, allowlisted forwarding
       v
Ollama (127.0.0.1:11434)
```

## What I did

- audited a Windows development environment and recorded reproducible baselines;
- investigated the Open-LLM-VTuber architecture and integration points;
- designed and tested a loopback-only FastAPI gateway for local models;
- added bearer authentication, model/backend allowlists, streaming support,
  timeouts, safe error handling, and health checks;
- prepared a PowerShell runbook with startup, smoke-test, rollback, and
  troubleshooting procedures;
- benchmarked OpenRouter models for availability, tool calling, response
  quality, latency, and provider errors;
- kept experiment reports and evidence so conclusions can be reviewed instead
  of relying on an unverified demo.

AI tools helped generate and investigate parts of the work. I defined the task,
reviewed the output, checked assumptions against the code and runtime, designed
the acceptance criteria, and retained evidence for the final conclusions.

## Repository map

| Path | Purpose |
|---|---|
| `local-agent-gateway/` | Security boundary and OpenAI-compatible proxy |
| `Open-LLM-VTuber/` | Upstream-based voice/Live2D client used for integration |
| `evidence/` | Environment audits, benchmarks, reports, and screenshots |
| `docs/praktikum_codex_hermes_full_windows_macos_ru_v3.pdf` | Full 77-page Russian practicum (PDF) |
| `docs/praktikum_codex_hermes_full_windows_macos_ru_v3.docx` | Editable practicum source (DOCX) |

The two codebases are Git submodules. Clone them together:

```bash
git clone --recurse-submodules https://github.com/aka-gst/agent-lab.git
```

## Quality gates

The gateway test suite covers:

- public health checks;
- required authentication;
- model and backend allowlists;
- streaming and non-streaming forwarding;
- upstream failures and timeout behavior;
- redaction-safe error responses.

Run it from `local-agent-gateway/`:

```bash
uv run pytest -q
```

A full end-to-end check also verifies Ollama, the gateway, and the VTuber UI on
their expected local ports. See the gateway README and the final practicum for
the complete procedure.

## Model evaluation

`evidence/benchmark_openrouter.py` performs a small, repeatable screening of
candidate models. It records:

- request success and provider failures;
- tool-selection and argument accuracy;
- rubric-based implementation-plan checks;
- median latency;
- basic vision-route availability.

The benchmark is intentionally described as a screening experiment, not a
universal model ranking. Its sample size and free-tier constraints are stated
in the report.

## Security decisions

- gateway binding is fixed to loopback;
- chat requests require a separate local bearer token;
- models and backends are allowlisted;
- real tokens are never stored in the repository or command examples;
- configuration backups are treated as secrets;
- operational instructions avoid printing `.env` and `conf.yaml`.

## Results

The lab produced a working, documented path from a voice AI interface to a
local or hosted language model. The deliverables include a tested security
gateway, repeatable environment and model audits, a 15-experiment practicum,
cross-platform Windows/macOS commands, end-to-end smoke tests, rollback
procedures, fault injection, and a definition of done.

## Portfolio links

- [Full practicum (PDF)](docs/praktikum_codex_hermes_full_windows_macos_ru_v3.pdf)
- [Editable practicum (DOCX)](docs/praktikum_codex_hermes_full_windows_macos_ru_v3.docx)
- [Local Agent Gateway](https://github.com/aka-gst/local-agent-gateway)
- [GitHub profile](https://github.com/aka-gst)
