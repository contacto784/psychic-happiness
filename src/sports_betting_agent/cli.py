"""Command-line interface for the sports betting agent."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .agent import BettingAgent, BettingAgentConfig
from .models import BetCandidate


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze a slate of sports betting candidates.")
    parser.add_argument("slate", type=Path, help="Path to a JSON file containing bet candidates.")
    parser.add_argument("--bankroll", type=float, default=1000.0, help="Current bankroll amount.")
    parser.add_argument("--kelly-fraction", type=float, default=0.25, help="Fractional Kelly multiplier.")
    parser.add_argument("--max-stake-fraction", type=float, default=0.02, help="Maximum bankroll fraction per bet.")
    parser.add_argument("--minimum-edge", type=float, default=0.01, help="Minimum edge required to recommend a stake.")
    args = parser.parse_args()

    candidates = _load_candidates(args.slate)
    agent = BettingAgent(
        BettingAgentConfig(
            bankroll=args.bankroll,
            kelly_fraction=args.kelly_fraction,
            max_stake_fraction=args.max_stake_fraction,
            minimum_edge=args.minimum_edge,
        )
    )

    print("Responsible betting card: no recommendation guarantees profit.\n")
    for index, recommendation in enumerate(agent.analyze(candidates), start=1):
        candidate = recommendation.candidate
        book = f" at {candidate.sportsbook}" if candidate.sportsbook else ""
        print(f"{index}. {candidate.event} — {candidate.selection}{book}")
        print(f"   Confidence: {recommendation.confidence}")
        print(f"   Decimal odds: {recommendation.decimal_odds:.3f}")
        print(f"   Implied probability: {recommendation.implied_probability:.1%}")
        print(f"   Estimated edge: {recommendation.edge:.1%}")
        print(f"   EV per unit: {recommendation.expected_value_per_unit:.3f}")
        print(f"   Suggested stake: {recommendation.stake:.2f}")
        print(f"   Rationale: {recommendation.rationale}\n")


def _load_candidates(path: Path) -> list[BetCandidate]:
    with path.open(encoding="utf-8") as file:
        raw_candidates = json.load(file)

    if not isinstance(raw_candidates, list):
        raise ValueError("Slate JSON must be a list of bet candidates")

    return [BetCandidate(**candidate) for candidate in raw_candidates]


if __name__ == "__main__":
    main()
