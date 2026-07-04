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


@dataclass(frozen=True)
class TeamResearchSummary:
    """Aggregated research view for one team across a slate."""

    team: str
    events: list[str]
    markets: list[str]
    candidate_count: int
    average_estimated_probability: float
    average_edge: float
    positive_edge_count: int
    strong_edge_count: int
    signals: list[str]


@dataclass(frozen=True)
class TeamResearchReport:
    """Research report containing every team discovered in a slate."""

    summaries: list[TeamResearchSummary]
