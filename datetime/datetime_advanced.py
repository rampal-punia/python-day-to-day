"""
Datetime Advanced — Timezones, Timedelta & Date Arithmetic
============================================================
Production-grade datetime handling in Python.

Author: @rampal-punia
"""

from datetime import datetime, date, time, timedelta, timezone
from zoneinfo import ZoneInfo  # Python 3.9+
import calendar


# ═══════════════════════════════════════════════════
# 1. TIMEDELTA — Date/Time Arithmetic
# ═══════════════════════════════════════════════════

def demo_timedelta():
    now = datetime.now()
    print(f"    Now            : {now:%Y-%m-%d %H:%M:%S}")

    # Adding/subtracting time
    tomorrow = now + timedelta(days=1)
    yesterday = now - timedelta(days=1)
    next_week = now + timedelta(weeks=1)
    three_hours_ago = now - timedelta(hours=3)

    print(f"    Tomorrow       : {tomorrow:%Y-%m-%d}")
    print(f"    Yesterday      : {yesterday:%Y-%m-%d}")
    print(f"    Next week      : {next_week:%Y-%m-%d}")
    print(f"    3 hours ago    : {three_hours_ago:%H:%M:%S}")

    # Difference between dates
    birthday = datetime(2026, 12, 25)
    delta = birthday - now
    print(f"\n    Days to Dec 25 : {delta.days} days")
    print(f"    Total seconds  : {delta.total_seconds():,.0f}")

    # timedelta arithmetic
    work_day = timedelta(hours=8)
    work_week = work_day * 5
    print(f"\n    Work day       : {work_day}")
    print(f"    Work week      : {work_week}")
    print(f"    In hours       : {work_week.total_seconds() / 3600}")

    # Deadline calculator
    print(f"\n    📅 Deadline Calculator:")
    deadlines = {
        "Sprint end": timedelta(weeks=2),
        "Quarter end": timedelta(days=90),
        "Year end": timedelta(days=365),
    }
    for name, delta in deadlines.items():
        end_date = now + delta
        print(f"      {name:15s}: {end_date:%B %d, %Y} ({delta.days} days)")


# ═══════════════════════════════════════════════════
# 2. TIMEZONE HANDLING — The Right Way
# ═══════════════════════════════════════════════════

def demo_timezones():
    """
    GOLDEN RULE: Always store datetimes in UTC internally.
    Convert to local timezone only for display.
    """
    # Current time in UTC
    utc_now = datetime.now(timezone.utc)
    print(f"    UTC Now        : {utc_now:%Y-%m-%d %H:%M:%S %Z}")

    # Convert to various timezones (Python 3.9+ ZoneInfo)
    zones = {
        "New York": ZoneInfo("America/New_York"),
        "London": ZoneInfo("Europe/London"),
        "Tokyo": ZoneInfo("Asia/Tokyo"),
        "Mumbai": ZoneInfo("Asia/Kolkata"),
        "Sydney": ZoneInfo("Australia/Sydney"),
    }

    print(f"\n    🌍 World Clock:")
    for city, tz in zones.items():
        local_time = utc_now.astimezone(tz)
        print(f"      {city:12s}: {local_time:%I:%M %p %Z}")

    # ⚠️ NEVER use datetime.utcnow() — it returns naive datetime!
    # ✅ Use datetime.now(timezone.utc) instead
    naive = datetime.utcnow()     # ❌ No timezone info!
    aware = datetime.now(timezone.utc)  # ✅ Timezone-aware

    print(f"\n    ⚠️  utcnow() (naive) : {naive} — tzinfo={naive.tzinfo}")
    print(f"    ✅ now(utc) (aware)  : {aware} — tzinfo={aware.tzinfo}")

    # Create timezone-aware datetime
    meeting_ny = datetime(2026, 3, 15, 14, 30,
                          tzinfo=ZoneInfo("America/New_York"))
    meeting_tokyo = meeting_ny.astimezone(ZoneInfo("Asia/Tokyo"))
    print(f"\n    Meeting in NY    : {meeting_ny:%Y-%m-%d %I:%M %p %Z}")
    print(f"    Same in Tokyo   : {meeting_tokyo:%Y-%m-%d %I:%M %p %Z}")


# ═══════════════════════════════════════════════════
# 3. PARSING & FORMATTING
# ═══════════════════════════════════════════════════

def demo_parsing_formatting():
    # strftime — datetime → string
    now = datetime.now()
    formats = {
        "ISO 8601": "%Y-%m-%dT%H:%M:%S",
        "US format": "%m/%d/%Y",
        "EU format": "%d/%m/%Y",
        "Readable": "%B %d, %Y at %I:%M %p",
        "Day name": "%A, %B %d",
        "Compact": "%Y%m%d_%H%M%S",
    }

    print("    strftime formats:")
    for name, fmt in formats.items():
        print(f"      {name:12s}: {now.strftime(fmt)}")

    # strptime — string → datetime
    print("\n    strptime (string → datetime):")
    date_strings = [
        ("2026-02-15", "%Y-%m-%d"),
        ("15/02/2026", "%d/%m/%Y"),
        ("Feb 15, 2026 3:30 PM", "%b %d, %Y %I:%M %p"),
    ]
    for s, fmt in date_strings:
        parsed = datetime.strptime(s, fmt)
        print(f"      '{s}' → {parsed}")

    # ISO format (built-in)
    iso_str = now.isoformat()
    print(f"\n    isoformat()    : {iso_str}")
    parsed_back = datetime.fromisoformat(iso_str)
    print(f"    fromisoformat(): {parsed_back}")

    # Timestamp (epoch seconds)
    epoch = now.timestamp()
    print(f"\n    timestamp()        : {epoch}")
    print(f"    fromtimestamp()    : {datetime.fromtimestamp(epoch)}")


# ═══════════════════════════════════════════════════
# 4. DATE COMPARISONS & RANGES
# ═══════════════════════════════════════════════════

def demo_comparisons():
    today = date.today()

    # Date comparison
    deadline = date(2026, 6, 30)
    is_overdue = today > deadline
    days_until = (deadline - today).days

    print(f"    Today      : {today}")
    print(f"    Deadline   : {deadline}")
    print(f"    Overdue?   : {is_overdue}")
    print(f"    Days until : {days_until}")

    # Generate date range
    def date_range(start: date, end: date, step: int = 1):
        """Generate dates from start to end."""
        current = start
        while current <= end:
            yield current
            current += timedelta(days=step)

    print(f"\n    Next 7 days:")
    for d in date_range(today, today + timedelta(days=6)):
        day_name = d.strftime("%A")
        is_weekend = d.weekday() >= 5
        marker = "🏖️" if is_weekend else "💼"
        print(f"      {marker} {d:%Y-%m-%d} ({day_name})")

    # Business days calculator
    def business_days_between(start: date, end: date) -> int:
        """Count business days (Mon-Fri) between two dates."""
        count = 0
        current = start
        while current <= end:
            if current.weekday() < 5:  # 0=Mon, 4=Fri
                count += 1
            current += timedelta(days=1)
        return count

    next_month = today + timedelta(days=30)
    bdays = business_days_between(today, next_month)
    print(f"\n    Business days in next 30 days: {bdays}")


# ═══════════════════════════════════════════════════
# 5. CALENDAR MODULE — Useful Utilities
# ═══════════════════════════════════════════════════

def demo_calendar():
    year, month = 2026, 2

    # Month calendar
    cal = calendar.TextCalendar()
    print(f"    📅 Calendar for {calendar.month_name[month]} {year}:")
    for line in cal.formatmonth(year, month).split("\n"):
        if line.strip():
            print(f"    {line}")

    # Useful calendar functions
    print(f"\n    Is 2024 leap year? : {calendar.isleap(2024)}")
    print(f"    Is 2026 leap year? : {calendar.isleap(2026)}")
    print(f"    Leap years 2020-2030: {calendar.leapdays(2020, 2030)}")

    # First weekday and days in month
    first_day, num_days = calendar.monthrange(year, month)
    day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    print(f"    {calendar.month_name[month]} {year}:")
    print(f"      Starts on : {day_names[first_day]}")
    print(f"      Total days: {num_days}")

    # All Fridays in a month
    fridays = [
        date(year, month, day)
        for day in range(1, num_days + 1)
        if date(year, month, day).weekday() == 4
    ]
    print(f"      Fridays   : {[f.day for f in fridays]}")


# ═══════════════════════════════════════════════════
# 6. REAL-WORLD: Countdown Timer & Age Calculator
# ═══════════════════════════════════════════════════

def demo_practical():
    now = datetime.now()

    # Countdown to events
    events = {
        "🎆 New Year 2027": datetime(2027, 1, 1),
        "🌍 Earth Day": datetime(2026, 4, 22),
        "🎃 Halloween": datetime(2026, 10, 31),
    }

    print("    ⏰ Countdown:")
    for name, event_date in events.items():
        delta = event_date - now
        if delta.days >= 0:
            hours = delta.seconds // 3600
            minutes = (delta.seconds % 3600) // 60
            print(f"      {name}: {delta.days}d {hours}h {minutes}m")
        else:
            print(f"      {name}: Already passed!")

    # Precise age calculator
    def calculate_age(birth_date: date) -> dict:
        today = date.today()
        years = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            years -= 1

        # Days until next birthday
        next_bday = date(today.year, birth_date.month, birth_date.day)
        if next_bday < today:
            next_bday = date(today.year + 1, birth_date.month, birth_date.day)
        days_until_bday = (next_bday - today).days

        total_days = (today - birth_date).days

        return {
            "years": years,
            "total_days": total_days,
            "total_weeks": total_days // 7,
            "days_until_birthday": days_until_bday,
        }

    birth = date(1995, 7, 20)
    age = calculate_age(birth)
    print(f"\n    🎂 Age Calculator (born {birth}):")
    print(f"      Age        : {age['years']} years")
    print(f"      Total days : {age['total_days']:,}")
    print(f"      Total weeks: {age['total_weeks']:,}")
    print(f"      Next birthday in {age['days_until_birthday']} days")


# ─────────────────────────────────────────────────
# DEMO
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    sections = [
        ("1. Timedelta — Date Arithmetic", demo_timedelta),
        ("2. Timezone Handling", demo_timezones),
        ("3. Parsing & Formatting", demo_parsing_formatting),
        ("4. Comparisons & Ranges", demo_comparisons),
        ("5. Calendar Module", demo_calendar),
        ("6. Practical — Countdown & Age", demo_practical),
    ]
    for title, fn in sections:
        print("\n" + "=" * 55)
        print(title)
        print("=" * 55)
        fn()
