"""Odds conversion helpers."""

from __future__ import annotations

from fractions import Fraction


def to_decimal_odds(odds: str | float | int) -> float:
    """Convert American, decimal, or fractional odds to decimal odds."""

    if isinstance(odds, (float, int)):
        decimal_odds = float(odds)
    else:
        text = odds.strip()
        if "/" in text:
            decimal_odds = float(Fraction(text)) + 1.0
        elif text.startswith(('+', '-')):
            american = int(text)
            decimal_odds = american_to_decimal(american)
        else:
            decimal_odds = float(text)

    if decimal_odds <= 1.0:
        raise ValueError("Decimal odds must be greater than 1.0")
    return decimal_odds


def american_to_decimal(american_odds: int) -> float:
    """Convert American odds to decimal odds."""

    if american_odds == 0:
        raise ValueError("American odds cannot be zero")
    if american_odds > 0:
        return 1.0 + american_odds / 100.0
    return 1.0 + 100.0 / abs(american_odds)


def implied_probability(decimal_odds: float) -> float:
    """Return the break-even probability implied by decimal odds."""

    if decimal_odds <= 1.0:
        raise ValueError("Decimal odds must be greater than 1.0")
    return 1.0 / decimal_odds
