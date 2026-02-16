"""Using the datetime Module — Dates, times, and comparisons.

Difficulty: 🟢 Easy
Topics: datetime, date, today(), date attributes, date comparison

The datetime module provides classes:
    datetime  — date + time combined
    date      — date only (year, month, day)
    time      — time only (hour, minute, second)
    timedelta — duration between two dates

Author: @rampal-punia
"""

from datetime import datetime


def explore_datetime_attributes() -> None:
    """Show how to extract parts from a datetime object."""
    now = datetime.today()

    print("── Datetime Attributes ──")
    print(f"  Full datetime:  {now}")
    print(f"  Date part:      {now.date()}")
    print(f"  Year:           {now.year}")
    print(f"  Month:          {now.month}")
    print(f"  Day:            {now.day}")
    print(f"  Hour:           {now.hour}")
    print(f"  Minute:         {now.minute}")
    print(f"  Second:         {now.second}")
    print(f"  Weekday:        {now.weekday()} (0=Mon, 6=Sun)")
    print(f"  Day name:       {now.strftime('%A')}")


def compare_dates() -> None:
    """Demonstrate date comparison operators."""
    today = datetime.today()
    past_date = datetime(2023, 4, 15)
    future_date = datetime(2030, 12, 31)

    print("\n── Date Comparisons ──")
    for label, dt in [("Past", past_date), ("Future", future_date)]:
        if today < dt:
            status = "is in the future"
        elif today.date() == dt.date():
            status = "is TODAY!"
        else:
            status = "has already passed"
        print(f"  {dt.date()} {status}")

    # Timedelta
    diff = future_date - today
    print(f"\n  Days until {future_date.date()}: {diff.days} days")


if __name__ == "__main__":
    explore_datetime_attributes()
    compare_dates()
