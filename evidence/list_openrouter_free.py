from __future__ import annotations

import json
import urllib.request
from datetime import date

URL = "https://openrouter.ai/api/v1/models"

with urllib.request.urlopen(URL, timeout=30) as response:
    models = json.load(response)["data"]

rows = []
for model in models:
    pricing = model.get("pricing") or {}

    if str(pricing.get("prompt")) != "0":
        continue
    if str(pricing.get("completion")) != "0":
        continue

    params = set(model.get("supported_parameters") or [])
    inputs = set(
        (model.get("architecture") or {}).get("input_modalities") or []
    )

    rows.append(
        {
            "id": model["id"],
            "context": model.get("context_length") or 0,
            "tools": "tools" in params,
            "vision": "image" in inputs,
            "expires": model.get("expiration_date") or "",
        }
    )

rows.sort(
    key=lambda row: (row["tools"], row["vision"], row["context"]),
    reverse=True,
)

print(f"Проверено: {date.today().isoformat()}")

for row in rows:
    print(
        f'{row["id"]:55} '
        f'ctx={row["context"]:>8} '
        f'tools={str(row["tools"]):5} '
        f'vision={str(row["vision"]):5} '
        f'expires={row["expires"] or "-"}'
    )