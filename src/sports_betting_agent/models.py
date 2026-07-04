"""Data models used by the sports betting agent."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BetCandidate:
    """A potential wager supplied to the betting agent."""

    event: str
    market: str
    selection: str
    odds: str | float | int
    estimated_probability: float
    sportsbook: str | None = None


@dataclass(frozen=True)
class BetRecommendation:
    """Agent output for a single candidate wager."""

    candidate: BetCandidate
    decimal_odds: float
    implied_probability: float
    edge: float
    expected_value_per_unit: float
    stake: float
    confidence: str
    rationale: str
