"""
String Methods — Complete Reference with Examples
===================================================
Every essential string method with practical usage.

Author: @rampal-punia
"""


# ═══════════════════════════════════════════════════
# 1. CASE METHODS
# ═══════════════════════════════════════════════════

def demo_case_methods():
    text = "hello, WORLD! python 3.12"

    methods = {
        "upper()":      text.upper(),           # HELLO, WORLD! PYTHON 3.12
        "lower()":      text.lower(),           # hello, world! python 3.12
        "title()":      text.title(),           # Hello, World! Python 3.12
        "capitalize()": text.capitalize(),      # Hello, world! python 3.12
        "swapcase()":   text.swapcase(),        # HELLO, world! PYTHON 3.12
        "casefold()":   text.casefold(),        # hello, world! python 3.12 (stronger lower)
    }
    for method, result in methods.items():
        print(f"    {method:16s} → {result!r}")

    # casefold vs lower — matters for non-ASCII
    german = "Straße"  # German street
    print(f"\n    'Straße'.lower()    → {german.lower()!r}")     # 'straße'
    print(f"    'Straße'.casefold() → {german.casefold()!r}")    # 'strasse'


# ═══════════════════════════════════════════════════
# 2. SEARCH & FIND
# ═══════════════════════════════════════════════════

def demo_search_methods():
    text = "Python is amazing and Python is powerful"

    print(f"    find('Python')      → {text.find('Python')}")        # 0
    print(f"    find('Python', 1)   → {text.find('Python', 1)}")     # 22
    print(f"    find('Java')        → {text.find('Java')}")          # -1 (not found)
    print(f"    rfind('Python')     → {text.rfind('Python')}")       # 22 (last occurrence)
    print(f"    index('Python')     → {text.index('Python')}")       # 0 (raises ValueError if missing)
    print(f"    count('Python')     → {text.count('Python')}")       # 2
    print(f"    startswith('Py')    → {text.startswith('Py')}")      # True
    print(f"    endswith('ful')     → {text.endswith('ful')}")       # True

    # startswith/endswith with tuple (check multiple)
    filename = "report.pdf"
    print(f"    Is document? → {filename.endswith(('.pdf', '.docx', '.txt'))}")


# ═══════════════════════════════════════════════════
# 3. SPLIT & JOIN
# ═══════════════════════════════════════════════════

def demo_split_join():
    csv_line = "Alice,28,Developer,New York"

    # split
    parts = csv_line.split(",")
    print(f"    split(',')          → {parts}")

    # split with maxsplit
    first_two = csv_line.split(",", maxsplit=2)
    print(f"    split(',', max=2)   → {first_two}")

    # rsplit (split from right)
    path = "/home/user/documents/file.txt"
    print(f"    rsplit('/', max=1)  → {path.rsplit('/', maxsplit=1)}")

    # splitlines
    text = "Line 1\nLine 2\nLine 3"
    print(f"    splitlines()        → {text.splitlines()}")

    # join — the opposite of split
    words = ["Python", "is", "awesome"]
    print(f"    ' '.join(words)     → {' '.join(words)}")
    print(f"    ' → '.join(words)   → {' → '.join(words)}")
    print(f"    ','.join(words)     → {','.join(words)}")

    # Practical: CSV from list
    data = ["Alice", "28", "NYC"]
    print(f"    CSV line            → {','.join(data)}")


# ═══════════════════════════════════════════════════
# 4. STRIP & CLEAN
# ═══════════════════════════════════════════════════

def demo_strip_methods():
    text = "   \t Hello, Python!  \n  "

    print(f"    Original   : {text!r}")
    print(f"    strip()    : {text.strip()!r}")
    print(f"    lstrip()   : {text.lstrip()!r}")
    print(f"    rstrip()   : {text.rstrip()!r}")

    # strip specific characters
    url = "///path/to/resource///"
    print(f"    strip('/')  : {url.strip('/')!r}")

    # removeprefix / removesuffix (Python 3.9+)
    filename = "test_module.py"
    print(f"    removeprefix('test_') : {filename.removeprefix('test_')!r}")
    print(f"    removesuffix('.py')   : {filename.removesuffix('.py')!r}")


# ═══════════════════════════════════════════════════
# 5. REPLACE & TRANSLATE
# ═══════════════════════════════════════════════════

def demo_replace_translate():
    text = "Hello World Hello Python"

    # replace
    print(f"    replace('Hello', 'Hi')   → {text.replace('Hello', 'Hi')}")
    print(f"    replace('Hello', 'Hi', 1)→ {text.replace('Hello', 'Hi', 1)}")

    # translate — character-level replacement (fast!)
    table = str.maketrans("aeiou", "12345")
    print(f"    translate vowels→nums    → {'python'.translate(table)}")

    # Remove characters with translate
    remove_punct = str.maketrans("", "", ".,!?;:")
    messy = "Hello, World! How are you? Fine; thanks."
    print(f"    Remove punctuation       → {messy.translate(remove_punct)}")


# ═══════════════════════════════════════════════════
# 6. CHECK / IS-METHODS
# ═══════════════════════════════════════════════════

def demo_is_methods():
    tests = {
        "'Hello'.isalpha()":     "Hello".isalpha(),       # True
        "'Hello1'.isalnum()":    "Hello1".isalnum(),      # True
        "'12345'.isdigit()":     "12345".isdigit(),       # True
        "'12345'.isnumeric()":   "12345".isnumeric(),     # True
        "'  '.isspace()":        "  ".isspace(),          # True
        "'Hello'.istitle()":     "Hello".istitle(),       # True
        "'HELLO'.isupper()":     "HELLO".isupper(),       # True
        "'hello'.islower()":     "hello".islower(),       # True
        "'abc'.isascii()":       "abc".isascii(),         # True
        "'x = 1'.isidentifier()": "x".isidentifier(),    # True
        "'print'.isidentifier()": "print".isidentifier(), # True
    }
    for expr, result in tests.items():
        symbol = "✅" if result else "❌"
        print(f"    {symbol} {expr:30s} → {result}")


# ═══════════════════════════════════════════════════
# 7. PADDING & ALIGNMENT
# ═══════════════════════════════════════════════════

def demo_padding():
    text = "Python"

    print(f"    center(20, '-')  → {text.center(20, '-')!r}")
    print(f"    ljust(20, '.')   → {text.ljust(20, '.')!r}")
    print(f"    rjust(20, '.')   → {text.rjust(20, '.')!r}")
    print(f"    zfill(10)        → {'42'.zfill(10)!r}")
    print(f"    zfill(10) neg    → {'-42'.zfill(10)!r}")

    # Practical: Table formatting
    data = [("Alice", 88), ("Bob", 95), ("Charlie", 72)]
    print("\n    ┌────────────┬───────┐")
    print("    │ Name       │ Score │")
    print("    ├────────────┼───────┤")
    for name, score in data:
        print(f"    │ {name.ljust(10)} │ {str(score).rjust(5)} │")
    print("    └────────────┴───────┘")


# ═══════════════════════════════════════════════════
# 8. SLICING — The Pythonic Way
# ═══════════════════════════════════════════════════

def demo_slicing():
    text = "Python Programming"

    print(f"    text[0:6]        → {text[0:6]!r}")       # 'Python'
    print(f"    text[7:]         → {text[7:]!r}")         # 'Programming'
    print(f"    text[-11:]       → {text[-11:]!r}")       # 'Programming'
    print(f"    text[::2]        → {text[::2]!r}")        # 'Pto rgamn'
    print(f"    text[::-1]       → {text[::-1]!r}")       # 'gnimmargorP nohtyP'

    # Practical: Extract parts
    email = "user@example.com"
    username = email[:email.index("@")]
    domain = email[email.index("@") + 1:]
    print(f"\n    Email   : {email}")
    print(f"    Username: {username}")
    print(f"    Domain  : {domain}")


# ─────────────────────────────────────────────────
# DEMO
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    sections = [
        ("1. Case Methods", demo_case_methods),
        ("2. Search & Find", demo_search_methods),
        ("3. Split & Join", demo_split_join),
        ("4. Strip & Clean", demo_strip_methods),
        ("5. Replace & Translate", demo_replace_translate),
        ("6. Is-Methods (Checks)", demo_is_methods),
        ("7. Padding & Alignment", demo_padding),
        ("8. String Slicing", demo_slicing),
    ]
    for title, fn in sections:
        print("\n" + "=" * 55)
        print(title)
        print("=" * 55)
        fn()
