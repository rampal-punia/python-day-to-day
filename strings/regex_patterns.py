"""
Regular Expressions — Pattern Matching with the re Module
==========================================================
Practical regex patterns every Python developer should know.

Author: @rampal-punia
"""

import re


# ═══════════════════════════════════════════════════
# REGEX CHEAT SHEET
# ═══════════════════════════════════════════════════
#
# CHARACTERS
#   .       Any character (except newline)
#   \d      Digit [0-9]              \D  Non-digit
#   \w      Word char [a-zA-Z0-9_]   \W  Non-word char
#   \s      Whitespace               \S  Non-whitespace
#   \b      Word boundary
#
# QUANTIFIERS
#   *       0 or more       +   1 or more
#   ?       0 or 1          {n} exactly n
#   {n,m}   n to m times
#
# ANCHORS
#   ^       Start of string     $   End of string
#
# GROUPS
#   (...)   Capture group    (?:...) Non-capture group
#   (?P<name>...) Named group
#
# FLAGS
#   re.IGNORECASE (re.I)    re.MULTILINE (re.M)
#   re.DOTALL (re.S)        re.VERBOSE (re.X)


# ─────────────────────────────────────────────────
# 1. BASIC OPERATIONS
# ─────────────────────────────────────────────────

def demo_basic_operations():
    text = "Contact us at support@example.com or sales@company.org"

    # search — find first match
    match = re.search(r"\w+@\w+\.\w+", text)
    if match:
        print(f"    search()  → {match.group()}")        # support@example.com
        print(f"    span()    → {match.span()}")          # (14, 34)

    # findall — find ALL matches
    emails = re.findall(r"\w+@\w+\.\w+", text)
    print(f"    findall() → {emails}")

    # finditer — find all with match objects
    print("    finditer():")
    for m in re.finditer(r"\w+@\w+\.\w+", text):
        print(f"      {m.group()} at position {m.start()}")

    # match — only at START of string
    result = re.match(r"Contact", text)
    print(f"    match()   → {result.group() if result else None}")

    # fullmatch — entire string must match
    result = re.fullmatch(r"\d{3}-\d{4}", "555-1234")
    print(f"    fullmatch → {result.group() if result else None}")


# ─────────────────────────────────────────────────
# 2. GROUPS — Capturing Parts of a Match
# ─────────────────────────────────────────────────

def demo_groups():
    # Basic groups
    date_text = "Today is 2026-02-15"
    match = re.search(r"(\d{4})-(\d{2})-(\d{2})", date_text)
    if match:
        print(f"    Full match : {match.group(0)}")
        print(f"    Year       : {match.group(1)}")
        print(f"    Month      : {match.group(2)}")
        print(f"    Day        : {match.group(3)}")
        print(f"    All groups : {match.groups()}")

    # Named groups (?P<name>...)
    log = '192.168.1.1 - - [15/Feb/2026:10:30:00] "GET /api/users HTTP/1.1" 200'
    pattern = r'(?P<ip>[\d.]+).*?"(?P<method>\w+)\s(?P<path>\S+)'
    match = re.search(pattern, log)
    if match:
        print(f"\n    Named groups:")
        print(f"      IP     : {match.group('ip')}")
        print(f"      Method : {match.group('method')}")
        print(f"      Path   : {match.group('path')}")
        print(f"      Dict   : {match.groupdict()}")


# ─────────────────────────────────────────────────
# 3. SUBSTITUTION — Search and Replace
# ─────────────────────────────────────────────────

def demo_substitution():
    # Basic replace
    text = "Call 555-123-4567 or 555-987-6543"
    censored = re.sub(r"\d{3}-\d{3}-\d{4}", "XXX-XXX-XXXX", text)
    print(f"    Censored: {censored}")

    # Replace with captured groups
    date = "15/02/2026"
    iso = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", date)
    print(f"    ISO date: {iso}")    # 2026-02-15

    # Replace with function
    text = "I have 3 cats and 12 dogs"
    result = re.sub(r"\d+", lambda m: str(int(m.group()) * 2), text)
    print(f"    Doubled : {result}")  # I have 6 cats and 24 dogs

    # subn — returns count of replacements
    text = "aaa bbb aaa"
    result, count = re.subn(r"aaa", "xxx", text)
    print(f"    subn    : {result} ({count} replacements)")


# ─────────────────────────────────────────────────
# 4. SPLITTING — More Powerful than str.split()
# ─────────────────────────────────────────────────

def demo_split():
    # Split on multiple delimiters
    text = "one,two;three four\tfive"
    parts = re.split(r"[,;\s]+", text)
    print(f"    Multi-split   : {parts}")

    # Split keeping delimiters (use capturing group)
    text = "Hello. How are you? I'm fine!"
    parts = re.split(r"([.?!])\s*", text)
    print(f"    Keep delims   : {parts}")

    # maxsplit
    text = "a:b:c:d:e"
    parts = re.split(r":", text, maxsplit=2)
    print(f"    maxsplit=2    : {parts}")    # ['a', 'b', 'c:d:e']


# ─────────────────────────────────────────────────
# 5. REAL-WORLD PATTERNS
# ─────────────────────────────────────────────────

PATTERNS = {
    "Email": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "Phone (US)": r"^\+?1?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$",
    "URL": r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/\S*)?$",
    "IPv4": r"^(\d{1,3}\.){3}\d{1,3}$",
    "Strong Password": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
    "Date (YYYY-MM-DD)": r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$",
    "Hex Color": r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$",
}


def demo_real_world():
    test_cases = [
        ("Email", "user@example.com", True),
        ("Email", "invalid.email", False),
        ("Phone (US)", "+1 (555) 123-4567", True),
        ("URL", "https://www.python.org/docs", True),
        ("IPv4", "192.168.1.1", True),
        ("Strong Password", "MyP@ss1word", True),
        ("Strong Password", "weak", False),
        ("Date (YYYY-MM-DD)", "2026-02-15", True),
        ("Hex Color", "#FF5733", True),
    ]

    for name, test, expected in test_cases:
        result = bool(re.match(PATTERNS[name], test))
        status = "✅" if result == expected else "❌"
        print(f"    {status} {name:20s} | {test:25s} → {result}")


# ─────────────────────────────────────────────────
# 6. COMPILED PATTERNS — Performance Optimization
# ─────────────────────────────────────────────────

def demo_compiled():
    """Compile regex once, use many times — faster for repeated use."""
    email_pattern = re.compile(
        r"""
        ^                       # start
        [a-zA-Z0-9._%+-]+       # username
        @                       # @ symbol
        [a-zA-Z0-9.-]+          # domain
        \.                      # dot
        [a-zA-Z]{2,}            # TLD
        $                       # end
        """,
        re.VERBOSE              # allows comments & whitespace in pattern
    )

    emails = [
        "alice@example.com",
        "bob@company.co.uk",
        "invalid@",
        "@nouser.com",
        "test@test.org",
    ]

    for email in emails:
        valid = bool(email_pattern.match(email))
        symbol = "✅" if valid else "❌"
        print(f"    {symbol} {email}")


# ─────────────────────────────────────────────────
# 7. TEXT PROCESSING — Extract Structured Data
# ─────────────────────────────────────────────────

def demo_text_processing():
    """Extract structured data from unstructured text."""

    log_data = """
    [2026-02-15 10:30:01] INFO  Server started on port 8080
    [2026-02-15 10:30:05] ERROR Database connection failed
    [2026-02-15 10:30:10] WARN  High memory usage: 85%
    [2026-02-15 10:30:15] INFO  Request from 192.168.1.42
    """

    pattern = re.compile(
        r"\[(?P<timestamp>[\d\-\s:]+)\]\s+"
        r"(?P<level>\w+)\s+"
        r"(?P<message>.+)"
    )

    print("    Parsed log entries:")
    for match in pattern.finditer(log_data):
        d = match.groupdict()
        level_icon = {"INFO": "ℹ️", "ERROR": "❌", "WARN": "⚠️"}.get(d["level"], "•")
        print(f"      {level_icon} [{d['timestamp'].strip()}] {d['message'].strip()}")


# ─────────────────────────────────────────────────
# DEMO
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    sections = [
        ("1. Basic Operations", demo_basic_operations),
        ("2. Groups & Named Groups", demo_groups),
        ("3. Substitution", demo_substitution),
        ("4. Splitting", demo_split),
        ("5. Real-World Patterns", demo_real_world),
        ("6. Compiled Patterns", demo_compiled),
        ("7. Text Processing", demo_text_processing),
    ]
    for title, fn in sections:
        print("\n" + "=" * 55)
        print(title)
        print("=" * 55)
        fn()
