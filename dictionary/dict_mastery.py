"""
Dictionary Comprehensions & Advanced Patterns
===============================================
From basics to production-grade dictionary techniques.

Author: @rampal-punia
"""

from collections import defaultdict, Counter
from itertools import groupby
from operator import itemgetter


# ═══════════════════════════════════════════════════
# 1. DICTIONARY COMPREHENSIONS
# ═══════════════════════════════════════════════════

def demo_comprehensions():
    """Dict comprehensions — {key: value for item in iterable}"""

    # Basic: squares
    squares = {n: n**2 for n in range(1, 6)}
    print(f"    Squares      : {squares}")

    # Filtering
    scores = {"Alice": 88, "Bob": 55, "Charlie": 92, "Diana": 45}
    passed = {k: v for k, v in scores.items() if v >= 60}
    print(f"    Passed (≥60) : {passed}")

    # Swap keys and values
    inverted = {v: k for k, v in scores.items()}
    print(f"    Inverted     : {inverted}")

    # From two lists (zip)
    keys = ["name", "age", "city"]
    values = ["Alice", 28, "NYC"]
    person = dict(zip(keys, values))
    print(f"    From zip     : {person}")

    # Conditional value
    numbers = range(-3, 4)
    sign_map = {n: ("+" if n > 0 else "-" if n < 0 else "0") for n in numbers}
    print(f"    Signs        : {sign_map}")

    # Nested comprehension — frequency map
    text = "hello world"
    freq = {ch: text.count(ch) for ch in set(text) if ch != " "}
    print(f"    Char freq    : {freq}")


# ═══════════════════════════════════════════════════
# 2. MERGING DICTIONARIES
# ═══════════════════════════════════════════════════

def demo_merging():
    defaults = {"theme": "light", "lang": "en", "font_size": 14}
    user_prefs = {"theme": "dark", "font_size": 16}

    # Method 1: unpacking (Python 3.5+) — right wins
    merged = {**defaults, **user_prefs}
    print(f"    ** unpacking   : {merged}")

    # Method 2: | operator (Python 3.9+)
    merged2 = defaults | user_prefs
    print(f"    | operator     : {merged2}")

    # Method 3: |= in-place merge (Python 3.9+)
    config = defaults.copy()
    config |= user_prefs
    print(f"    |= in-place    : {config}")

    # Method 4: update() — modifies in-place
    config2 = defaults.copy()
    config2.update(user_prefs)
    print(f"    .update()      : {config2}")

    # Merge multiple dicts
    a, b, c = {"x": 1}, {"y": 2}, {"z": 3}
    merged_all = {**a, **b, **c}
    print(f"    Multi-merge    : {merged_all}")


# ═══════════════════════════════════════════════════
# 3. SAFE ACCESS — get(), setdefault(), defaultdict
# ═══════════════════════════════════════════════════

def demo_safe_access():
    data = {"name": "Alice", "age": 28}

    # get() — returns default instead of KeyError
    print(f"    get('name')       : {data.get('name')}")
    print(f"    get('city')       : {data.get('city')}")           # None
    print(f"    get('city', 'N/A'): {data.get('city', 'N/A')}")   # 'N/A'

    # setdefault() — get OR set if missing
    data.setdefault("city", "Unknown")  # sets 'city' since it's missing
    data.setdefault("name", "Bob")      # doesn't overwrite — 'name' exists
    print(f"    After setdefault  : {data}")

    # defaultdict — auto-creates missing keys
    word_lists = defaultdict(list)
    words = [("fruit", "apple"), ("veggie", "carrot"), ("fruit", "banana"),
             ("veggie", "pea"), ("fruit", "cherry")]

    for category, item in words:
        word_lists[category].append(item)  # no need to check if key exists
    print(f"    defaultdict(list) : {dict(word_lists)}")

    # defaultdict(int) — perfect for counting
    counter = defaultdict(int)
    for char in "mississippi":
        counter[char] += 1
    print(f"    defaultdict(int)  : {dict(counter)}")


# ═══════════════════════════════════════════════════
# 4. ITERATION PATTERNS
# ═══════════════════════════════════════════════════

def demo_iteration():
    scores = {"Alice": 88, "Bob": 95, "Charlie": 72, "Diana": 91}

    # Keys (default)
    print(f"    keys()   : {list(scores.keys())}")

    # Values
    print(f"    values() : {list(scores.values())}")

    # Items (key-value pairs)
    print(f"    items()  : {list(scores.items())}")

    # Iterate with index
    print("    Enumerated:")
    for i, (name, score) in enumerate(scores.items(), 1):
        print(f"      {i}. {name}: {score}")


# ═══════════════════════════════════════════════════
# 5. SORTING DICTIONARIES
# ═══════════════════════════════════════════════════

def demo_sorting():
    scores = {"Alice": 88, "Bob": 95, "Charlie": 72, "Diana": 91}

    # Sort by key
    by_key = dict(sorted(scores.items()))
    print(f"    By key (asc)   : {by_key}")

    # Sort by value
    by_val = dict(sorted(scores.items(), key=lambda x: x[1]))
    print(f"    By value (asc) : {by_val}")

    # Sort by value descending
    by_val_desc = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
    print(f"    By value (desc): {by_val_desc}")

    # Using operator.itemgetter (faster)
    by_val_ig = dict(sorted(scores.items(), key=itemgetter(1), reverse=True))
    print(f"    itemgetter     : {by_val_ig}")

    # Top N items
    top_2 = dict(sorted(scores.items(), key=itemgetter(1), reverse=True)[:2])
    print(f"    Top 2 scores   : {top_2}")


# ═══════════════════════════════════════════════════
# 6. NESTED DICTIONARIES
# ═══════════════════════════════════════════════════

def demo_nested():
    # Nested dict
    company = {
        "engineering": {
            "Alice": {"role": "Lead", "salary": 150_000},
            "Bob": {"role": "Senior", "salary": 130_000},
        },
        "marketing": {
            "Charlie": {"role": "Director", "salary": 140_000},
        },
    }

    # Safe nested access
    def deep_get(d: dict, *keys, default=None):
        """Safely traverse nested dicts without KeyError."""
        for key in keys:
            if isinstance(d, dict):
                d = d.get(key, default)
            else:
                return default
        return d

    print(f"    Alice's role   : {deep_get(company, 'engineering', 'Alice', 'role')}")
    print(f"    Missing path   : {deep_get(company, 'hr', 'Eve', 'role', default='N/A')}")

    # Flatten nested dict
    def flatten_dict(d: dict, parent_key: str = "", sep: str = ".") -> dict:
        items = {}
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(flatten_dict(v, new_key, sep))
            else:
                items[new_key] = v
        return items

    flat = flatten_dict(company)
    print(f"\n    Flattened:")
    for key, val in flat.items():
        print(f"      {key}: {val}")


# ═══════════════════════════════════════════════════
# 7. DICT UNPACKING & KWARGS PATTERN
# ═══════════════════════════════════════════════════

def demo_unpacking():
    def create_user(name: str, age: int, city: str = "Unknown") -> dict:
        return {"name": name, "age": age, "city": city}

    # Unpack dict as keyword arguments
    user_data = {"name": "Alice", "age": 28, "city": "NYC"}
    user = create_user(**user_data)
    print(f"    **kwargs unpack: {user}")

    # Selective extraction
    full = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    keep = {"a", "c", "e"}
    subset = {k: v for k, v in full.items() if k in keep}
    print(f"    Subset         : {subset}")

    # Remove keys
    remove = {"b", "d"}
    filtered = {k: v for k, v in full.items() if k not in remove}
    print(f"    Filtered       : {filtered}")


# ═══════════════════════════════════════════════════
# 8. REAL-WORLD: GROUPING & AGGREGATION
# ═══════════════════════════════════════════════════

def demo_real_world():
    """Group and aggregate data — a common data processing task."""
    transactions = [
        {"user": "Alice", "amount": 50.0, "category": "food"},
        {"user": "Bob", "amount": 120.0, "category": "tech"},
        {"user": "Alice", "amount": 30.0, "category": "food"},
        {"user": "Charlie", "amount": 200.0, "category": "tech"},
        {"user": "Bob", "amount": 45.0, "category": "food"},
        {"user": "Alice", "amount": 80.0, "category": "tech"},
    ]

    # Group by user — total spending
    spending = defaultdict(float)
    for t in transactions:
        spending[t["user"]] += t["amount"]
    print(f"    User spending  : {dict(spending)}")

    # Group by category — list of amounts
    by_category = defaultdict(list)
    for t in transactions:
        by_category[t["category"]].append(t["amount"])
    print(f"    By category    : {dict(by_category)}")

    # Pivot: user → category → total
    pivot = defaultdict(lambda: defaultdict(float))
    for t in transactions:
        pivot[t["user"]][t["category"]] += t["amount"]
    print(f"    Pivot table:")
    for user, cats in pivot.items():
        print(f"      {user:10s}: {dict(cats)}")


# ─────────────────────────────────────────────────
# DEMO
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    sections = [
        ("1. Dictionary Comprehensions", demo_comprehensions),
        ("2. Merging Dictionaries", demo_merging),
        ("3. Safe Access Patterns", demo_safe_access),
        ("4. Iteration Patterns", demo_iteration),
        ("5. Sorting Dictionaries", demo_sorting),
        ("6. Nested Dictionaries", demo_nested),
        ("7. Unpacking & kwargs", demo_unpacking),
        ("8. Real-World Grouping", demo_real_world),
    ]
    for title, fn in sections:
        print("\n" + "=" * 55)
        print(title)
        print("=" * 55)
        fn()
