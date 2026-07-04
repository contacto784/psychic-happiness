# Sports Betting Agent

A responsible, data-driven sports betting assistant that evaluates betting opportunities from supplied odds and probability estimates. It does **not** promise wins or provide financial advice; it helps rank wagers using expected value and bankroll-management rules.

## Features

- Converts American, decimal, and fractional odds into decimal odds and implied probabilities.
- Calculates expected value (EV) for candidate bets.
- Recommends a conservative Kelly-fraction stake with a configurable maximum-risk cap.
- Produces a ranked betting card from JSON input.
- Includes responsible-gambling guardrails and transparent reasoning for every recommendation.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Run the CLI with the sample slate:

```bash
sports-betting-agent examples/sample_slate.json --bankroll 1000
```

## Input format

```json
[
  {
    "event": "Team A vs Team B",
    "market": "Moneyline",
    "selection": "Team A",
    "odds": "+140",
    "estimated_probability": 0.45,
    "sportsbook": "ExampleBook"
  }
]
```

`odds` can be American (`+140`, `-115`), decimal (`2.40`), or fractional (`7/5`). `estimated_probability` must be your model's probability from 0 to 1.

## Responsible use

Only bet what you can afford to lose. This tool is educational and analytical software, not a guarantee of profit. If betting stops being fun or feels difficult to control, consider using self-exclusion tools and seeking help from a qualified support organization.
