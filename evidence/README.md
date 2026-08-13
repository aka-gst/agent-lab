# Evidence index

This directory records how the integration was investigated and tested.
Evidence is retained to make conclusions reviewable and reproducible.

## Environment and repository audits

- `exp-01-environment.md` — Windows development environment inventory.
- `exp-02-environment.md` — Git topology and upstream relationship.
- `exp-03-environment_Kimi.md` — agent-assisted environment investigation.
- `exp-04-environment_ChatGPT.md` — comparative investigation notes.
- `exp-06-environment.md` — end-to-end installation and runtime transcript.
- `Open-LLM-VTuber-readonly-report.txt` — architecture read-only report.

## Model evaluation

- `benchmark_openrouter.py` — repeatable benchmark runner.
- `openrouter_benchmark_2026-07-29.md` — compact result report.
- `openrouter_benchmark_2026-07-29.json` — machine-readable results.
- `list_openrouter_free.py` and output — model discovery snapshot.

## Review guidance

The reports include dates, environment constraints, and known limitations.
Absolute local paths are evidence of the tested setup, not portable commands.
No report should contain API keys, passwords, private configuration files, or
unredacted user data.

Large raw logs should be reduced to a short redacted summary before this
repository is made public. Binary evidence that is not essential for review
belongs in a GitHub Release rather than the main branch.
