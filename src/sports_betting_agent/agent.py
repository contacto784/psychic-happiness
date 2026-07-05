"""Core betting recommendation engine."""

from __future__ import annotations

from dataclasses import dataclass

from .models import BetCandidate, BetRecommendation
from .odds import implied_probability, to_decimal_odds


@dataclass(frozen=True)
class BettingAgentConfig:
    """Risk controls for the betting agent."""

    bankroll: float = 1000.0
    kelly_fraction: float = 0.25
    max_stake_fraction: float = 0.02
    minimum_edge: float = 0.01

    def __post_init__(self) -> None:
        if self.bankroll <= 0:
            raise ValueError("bankroll must be positive")
        if not 0 < self.kelly_fraction <= 1:
            raise ValueError("kelly_fraction must be in the range (0, 1]")
        if not 0 < self.max_stake_fraction <= 1:
            raise ValueError("max_stake_fraction must be in the range (0, 1]")
        if self.minimum_edge < 0:
            raise ValueError("minimum_edge cannot be negative")


class BettingAgent:
    """Rank bet candidates by expected value with responsible staking limits."""

    def __init__(self, config: BettingAgentConfig | None = None) -> None:
        self.config = config or BettingAgentConfig()

    def analyze(self, candidates: list[BetCandidate]) -> list[BetRecommendation]:
        """Analyze and rank bet candidates by expected value."""

        recommendations = [self._recommend(candidate) for candidate in candidates]
        return sorted(
            recommendations,
            key=lambda recommendation: recommendation.expected_value_per_unit,
            reverse=True,
        )

    def _recommend(self, candidate: BetCandidate) -> BetRecommendation:
        probability = candidate.estimated_probability
        if not 0 < probability < 1:
            raise ValueError("estimated_probability must be between 0 and 1")

        decimal_odds = to_decimal_odds(candidate.odds)
        break_even = implied_probability(decimal_odds)
        edge = probability - break_even
        expected_value = probability * (decimal_odds - 1.0) - (1.0 - probability)
        stake = self._stake(decimal_odds, probability, edge)
        confidence = self._confidence(edge, expected_value)
        rationale = self._rationale(candidate, break_even, edge, expected_value, stake)

        return BetRecommendation(
            candidate=candidate,
            decimal_odds=decimal_odds,
            implied_probability=break_even,
            edge=edge,
            expected_value_per_unit=expected_value,
            stake=stake,
            confidence=confidence,
            rationale=rationale,
        )

    def _stake(self, decimal_odds: float, probability: float, edge: float) -> float:
        if edge < self.config.minimum_edge:
            return 0.0

        net_odds = decimal_odds - 1.0
        full_kelly_fraction = (probability * net_odds - (1.0 - probability)) / net_odds
        conservative_fraction = max(0.0, full_kelly_fraction * self.config.kelly_fraction)
        capped_fraction = min(conservative_fraction, self.config.max_stake_fraction)
        return round(self.config.bankroll * capped_fraction, 2)

    def _confidence(self, edge: float, expected_value: float) -> str:
        if edge < self.config.minimum_edge or expected_value <= 0:
            return "pass"
        if edge >= 0.05:
            return "strong"
        if edge >= 0.025:
            return "moderate"
        return "lean"

    @staticmethod
    def _rationale(
        candidate: BetCandidate,
        break_even: float,
        edge: float,
        expected_value: float,
        stake: float,
    ) -> str:
        action = "Consider" if stake > 0 else "Pass on"
        return (
            f"{action} {candidate.selection} in {candidate.market}: "
            f"model probability {candidate.estimated_probability:.1%} vs. "
            f"break-even {break_even:.1%}, edge {edge:.1%}, "
            f"EV {expected_value:.3f} units."
        )
