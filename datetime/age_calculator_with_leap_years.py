"""Age Calculator (Accurate) — Using dateutil.relativedelta for leap years.

Difficulty: 🟡 Intermediate
Topics: dateutil, relativedelta, leap year handling, precise age
Requires: pip install python-dateutil

Unlike dividing by 365, relativedelta properly accounts for:
  - Leap years (366-day years)
  - Varying month lengths (28/29/30/31 days)
  - Exact years + months + days breakdown

Author: @rampal-punia
"""

from datetime import date

import dateutil.relativedelta as rd


def calculate_age_precise(year: int, month: int, day: int) -> dict[str, object]:
    """Calculate precise age using relativedelta.

    Args:
        year: Birth year.
        month: Birth month (1-12).
        day: Birth day (1-31).

    Returns:
        Dict with 'dob', 'today', 'years', 'months', 'days', 'formatted'.
    """
    dob = date(year, month, day)
    today = date.today()
    diff = rd.relativedelta(today, dob)

    return {
        "dob": dob,
        "today": today,
        "years": diff.years,
        "months": diff.months,
        "days": diff.days,
        "formatted": f"{diff.years} years, {diff.months} months, {diff.days} days",
    }


if __name__ == "__main__":
    print("── Precise Age Calculator (with leap years) ──")
    result = calculate_age_precise(1995, 1, 1)
    for key, value in result.items():
        print(f"  {key:<10}: {value}")

# For more on Python follow: https://x.com/rs_punia_
