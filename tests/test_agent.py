from sports_betting_agent import BetCandidate, BettingAgent, BettingAgentConfig
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
