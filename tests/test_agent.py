from sports_betting_agent import BetCandidate, BettingAgent, BettingAgentConfig, TeamResearcher
from sports_betting_agent.odds import implied_probability, to_decimal_odds


def test_odds_conversion_supports_common_formats():
    assert to_decimal_odds("+140") == 2.4
    assert round(to_decimal_odds("-110"), 3) == 1.909
    assert to_decimal_odds("7/5") == 2.4
    assert to_decimal_odds(2.5) == 2.5


def test_implied_probability():
    assert implied_probability(2.0) == 0.5


def test_agent_recommends_positive_edge_and_passes_negative_edge():
    agent = BettingAgent(BettingAgentConfig(bankroll=1000, minimum_edge=0.01))
    recommendations = agent.analyze(
        [
            BetCandidate("A vs B", "Moneyline", "A", "+140", 0.45),
            BetCandidate("C vs D", "Moneyline", "C", "-110", 0.49),
        ]
    )

    assert recommendations[0].candidate.selection == "A"
    assert recommendations[0].confidence in {"lean", "moderate", "strong"}
    assert recommendations[0].stake > 0
    assert recommendations[1].confidence == "pass"
    assert recommendations[1].stake == 0


def test_team_researcher_summarizes_all_teams_in_slate():
    report = TeamResearcher().research(
        [
            BetCandidate("Brewers vs Diamondbacks", "Moneyline", "Brewers", "-135", 0.61),
            BetCandidate("Braves vs Mets", "Run Line -1.5", "Braves", "+125", 0.49),
            BetCandidate("Blue Jays @ Mariners", "Total Under 8", "Under", "-110", 0.54),
        ]
    )

    summaries = {summary.team: summary for summary in report.summaries}

    assert {"Brewers", "Diamondbacks", "Braves", "Mets", "Blue Jays", "Mariners"}.issubset(summaries)
    assert summaries["Brewers"].candidate_count == 1
    assert summaries["Brewers"].direct_candidate_count == 1
    assert summaries["Diamondbacks"].candidate_count == 1
    assert summaries["Diamondbacks"].direct_candidate_count == 0
    assert summaries["Blue Jays"].candidate_count == 1
    assert summaries["Mariners"].candidate_count == 1
    assert summaries["Brewers"].positive_edge_count == 1
