"""Command-line interface for the sports betting agent."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .agent import BettingAgent, BettingAgentConfig
from .models import BetCandidate
from .team_research import TeamResearcher


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze a slate of sports betting candidates.")
    parser.add_argument("slate", type=Path, help="Path to a JSON file containing bet candidates.")
    parser.add_argument("--bankroll", type=float, default=1000.0, help="Current bankroll amount.")
    parser.add_argument("--kelly-fraction", type=float, default=0.25, help="Fractional Kelly multiplier.")
    parser.add_argument("--max-stake-fraction", type=float, default=0.02, help="Maximum bankroll fraction per bet.")
    parser.add_argument("--minimum-edge", type=float, default=0.01, help="Minimum edge required to recommend a stake.")
    parser.add_argument(
        "--team-report",
        action="store_true",
        help="Print a deep research summary for every team detected in the slate.",
    )
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

    if args.team_report:
        _print_team_report(candidates)

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


def _print_team_report(candidates: list[BetCandidate]) -> None:
    report = TeamResearcher().research(candidates)
    print("Deep team research: all detected teams")
    print("Use this as a checklist for deeper injury, lineup, weather, schedule, and price checks.\n")
    for index, summary in enumerate(report.summaries, start=1):
        print(f"{index}. {summary.team}")
        print(f"   Events: {', '.join(summary.events)}")
        print(f"   Markets: {', '.join(summary.markets)}")
        print(f"   Candidate markets: {summary.candidate_count}")
        print(f"   Direct/team-neutral markets: {summary.direct_candidate_count}")
        print(f"   Avg model probability: {summary.average_estimated_probability:.1%}")
        print(f"   Avg edge: {summary.average_edge:.1%}")
        print(f"   Positive / strong edges: {summary.positive_edge_count} / {summary.strong_edge_count}")
        for signal in summary.signals:
            print(f"   - {signal}")
        print()


if __name__ == "__main__":
    main()
