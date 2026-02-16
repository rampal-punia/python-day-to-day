"""Age Calculator (Simple) — Calculate age from date of birth.

Difficulty: 🟢 Easy
Topics: datetime.date, timedelta, date arithmetic

Note: This version divides total days by 365, which is approximate.
See age_calculator_with_leap_years.py for an accurate version.

Author: @rampal-punia
"""

from datetime import date


def calculate_age_simple(year: int, month: int, day: int) -> dict[str, int | float]:
    """Calculate approximate age from a date of birth.

    Uses total_days / 365 (ignores leap years).

    Args:
        year: Birth year.
        month: Birth month (1-12).
        day: Birth day (1-31).

    Returns:
        Dict with 'dob', 'today', 'days', 'approx_years'.
    """
    dob = date(year, month, day)
    today = date.today()
    total_days = (today - dob).days
    approx_years = total_days / 365

    return {
        "dob": dob,
        "today": today,
        "days": total_days,
        "approx_years": round(approx_years, 2),
    }


if __name__ == "__main__":
    print("── Simple Age Calculator ──")
    result = calculate_age_simple(1995, 1, 1)
    for key, value in result.items():
        print(f"  {key:<14}: {value}")
    print("  (approximate — does not account for leap years)")

# For more on Python follow: https://x.com/rs_punia_
