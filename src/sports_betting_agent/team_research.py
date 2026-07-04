"""Team-level research helpers for the sports betting agent."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from statistics import mean

from .models import BetCandidate, TeamResearchReport, TeamResearchSummary
from .odds import implied_probability, to_decimal_odds


@dataclass(frozen=True)
class TeamResearchConfig:
    """Configuration for extracting team names and labeling team research."""

    event_separators: tuple[str, ...] = (" vs ", " @ ", " at ", " v ")
    strong_edge_threshold: float = 0.05
    positive_edge_threshold: float = 0.01


class TeamResearcher:
    """Build a transparent summary for every team found in a slate."""

    def __init__(self, config: TeamResearchConfig | None = None) -> None:
        self.config = config or TeamResearchConfig()

    def research(self, candidates: list[BetCandidate]) -> TeamResearchReport:
        """Return team summaries for all teams mentioned in the candidate slate."""

        teams = self._group_by_team(candidates)
        summaries = [self._summarize(team, team_candidates) for team, team_candidates in teams.items()]
        summaries.sort(key=lambda summary: (summary.average_edge, summary.average_estimated_probability), reverse=True)
        return TeamResearchReport(summaries=summaries)

    def _group_by_team(self, candidates: list[BetCandidate]) -> dict[str, list[BetCandidate]]:
        grouped: dict[str, list[BetCandidate]] = defaultdict(list)
        for candidate in candidates:
            teams = self._teams_for_candidate(candidate)
            for team in teams:
                grouped[team].append(candidate)
        return dict(grouped)

    def _teams_for_candidate(self, candidate: BetCandidate) -> list[str]:
        event_teams = self._parse_event_teams(candidate.event)
        if candidate.selection in event_teams:
            return [candidate.selection]
        return event_teams

    def _parse_event_teams(self, event: str) -> list[str]:
        for separator in self.config.event_separators:
            if separator in event:
                return [team.strip() for team in event.split(separator, maxsplit=1) if team.strip()]
        return [event.strip()] if event.strip() else []

    def _summarize(self, team: str, candidates: list[BetCandidate]) -> TeamResearchSummary:
        probabilities = [candidate.estimated_probability for candidate in candidates]
        edges = [self._edge(candidate) for candidate in candidates]
        positive_edges = sum(edge >= self.config.positive_edge_threshold for edge in edges)
        strong_edges = sum(edge >= self.config.strong_edge_threshold for edge in edges)
        markets = sorted({candidate.market for candidate in candidates})
        events = sorted({candidate.event for candidate in candidates})
        signals = self._signals(team, candidates, edges, positive_edges, strong_edges)

        return TeamResearchSummary(
            team=team,
            events=events,
            markets=markets,
            candidate_count=len(candidates),
            average_estimated_probability=round(mean(probabilities), 4),
            average_edge=round(mean(edges), 4),
            positive_edge_count=positive_edges,
            strong_edge_count=strong_edges,
            signals=signals,
        )

    @staticmethod
    def _edge(candidate: BetCandidate) -> float:
        decimal_odds = to_decimal_odds(candidate.odds)
        return candidate.estimated_probability - implied_probability(decimal_odds)

    def _signals(
        self,
        team: str,
        candidates: list[BetCandidate],
        edges: list[float],
        positive_edges: int,
        strong_edges: int,
    ) -> list[str]:
        signals = [
            f"Found {len(candidates)} candidate market(s) involving {team}.",
            f"Average modeled edge is {mean(edges):.1%} across available markets.",
        ]
        if strong_edges:
            signals.append(f"{strong_edges} market(s) clear the strong-edge threshold.")
        elif positive_edges:
            signals.append(f"{positive_edges} market(s) clear the minimum positive-edge threshold.")
        else:
            signals.append("No market currently clears the positive-edge threshold.")
        return signals
