# OpenRouter benchmark — 2026-07-29

| Model | Requests | Success | Tool use | Median latency | Plan | 429 | 5xx |
|---|---:|---:|---:|---:|---:|---:|---:|
| poolside/laguna-xs-2.1:free | 3 | 1 | 0/2 | 21671.8 ms | -/4 | 2 | 0 |
| cohere/north-mini-code:free | 6 | 6 | 4/4 | 3018.2 ms | 3.5/4 | 0 | 0 |

## Unavailable candidates

- Laguna M.1

## Vision

| Model | Success | Latency | HTTP |
|---|---:|---:|---:|
| google/gemma-4-26b-a4b-it:free | False | 2785.6 ms | 200 |
| google/gemma-4-31b-it:free | False | 474.6 ms | 429 |
| nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | False | 651.3 ms | 200 |
| nvidia/nemotron-nano-12b-v2-vl:free | False | 1143.2 ms | 502 |

## Selection

- Default: cohere/north-mini-code:free
- Fallback: not selected
- Vision route: not selected
- Rule: tool success rate, then plan score, then median latency; zero 429/5xx required

Automated plan scores are rubric checks, not a human semantic evaluation.
