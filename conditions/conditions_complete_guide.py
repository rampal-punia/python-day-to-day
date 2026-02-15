"""
Conditions & Control Flow — Complete Guide
============================================
From basics to advanced patterns including pattern matching.

Author: @rampal-punia
"""


# ═══════════════════════════════════════════════════
# 1. IF / ELIF / ELSE — Basics
# ═══════════════════════════════════════════════════

def demo_basic_conditions():
    score = 85

    # Standard if/elif/else
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"    Score {score} → Grade {grade}")


# ═══════════════════════════════════════════════════
# 2. TERNARY / CONDITIONAL EXPRESSION
# ═══════════════════════════════════════════════════

def demo_ternary():
    age = 20

    # Basic ternary: value_if_true if condition else value_if_false
    status = "adult" if age >= 18 else "minor"
    print(f"    Age {age} → {status}")

    # Nested ternary (use sparingly!)
    temp = 35
    comfort = "hot" if temp > 30 else "warm" if temp > 20 else "cold"
    print(f"    Temp {temp}°C → {comfort}")

    # Ternary in expressions
    numbers = [1, -2, 3, -4, 5]
    absolutes = [n if n >= 0 else -n for n in numbers]
    print(f"    Absolutes: {absolutes}")


# ═══════════════════════════════════════════════════
# 3. CHAINED COMPARISONS — Pythonic!
# ═══════════════════════════════════════════════════

def demo_chained_comparisons():
    """Python allows chaining comparisons — very clean and mathematical."""
    x = 15

    # ❌ Non-Pythonic
    result1 = x > 10 and x < 20
    print(f"    x > 10 and x < 20 : {result1}")

    # ✅ Pythonic — chained
    result2 = 10 < x < 20
    print(f"    10 < x < 20       : {result2}")

    # Multiple chains
    a, b, c = 1, 2, 3
    print(f"    1 <= 1 < 2 < 3    : {1 <= a < b < c}")
    print(f"    a == 1 == True    : {a == 1 == True}")   # True! (1 == True)

    # Range check
    age = 25
    is_working_age = 18 <= age <= 65
    print(f"    Working age (18-65): {is_working_age}")


# ═══════════════════════════════════════════════════
# 4. TRUTHY & FALSY VALUES
# ═══════════════════════════════════════════════════

def demo_truthy_falsy():
    """
    Falsy values: False, None, 0, 0.0, 0j, '', [], (), {}, set(), frozenset()
    Everything else is truthy.
    """
    falsy_values = [False, None, 0, 0.0, 0j, "", [], (), {}, set(), frozenset()]
    print("    Falsy values:")
    for val in falsy_values:
        print(f"      bool({str(val):15s}) → {bool(val)}")

    # Practical use — no need for explicit comparisons
    name = ""
    items = [1, 2, 3]
    data = None

    # ❌ Verbose
    if name != "":
        pass
    if len(items) > 0:
        pass
    if data is not None:
        pass

    # ✅ Pythonic — use truthiness
    if name:
        print("    Name is set")
    if items:
        print("    Items exist")
    if data:
        print("    Data available")

    print(f"\n    name='' → {'truthy' if name else 'falsy'}")
    print(f"    items=[1,2,3] → {'truthy' if items else 'falsy'}")
    print(f"    data=None → {'truthy' if data else 'falsy'}")


# ═══════════════════════════════════════════════════
# 5. SHORT-CIRCUIT EVALUATION
# ═══════════════════════════════════════════════════

def demo_short_circuit():
    """
    and → returns first falsy value, or last value if all truthy
    or  → returns first truthy value, or last value if all falsy
    """
    # 'or' for defaults
    name = "" or "Anonymous"
    print(f"    '' or 'Anonymous'        → {name!r}")

    config = None or {} or {"default": True}
    print(f"    None or {{}} or {{def}}     → {config}")

    # 'and' for guarded access
    data = {"user": {"name": "Alice"}}
    name = data and data.get("user") and data["user"].get("name")
    print(f"    Guarded access           → {name!r}")

    # Practical: default values
    port = 0 or 8080          # ⚠️ 0 is falsy! Use 'if x is None' instead
    print(f"    0 or 8080 (⚠️ pitfall)  → {port}")

    port = 0 if 0 is not None else 8080  # ✅ Correct for 0
    print(f"    0 if not None (correct)  → {port}")


# ═══════════════════════════════════════════════════
# 6. WALRUS OPERATOR := (Python 3.8+)
# ═══════════════════════════════════════════════════

def demo_walrus():
    """Assignment expression — assign and use in one step."""

    # ── In while loops ──
    import io
    stream = io.StringIO("line1\nline2\nline3\n")

    print("    Reading lines with :=")
    while (line := stream.readline().strip()):
        print(f"      Read: {line}")

    # ── In if statements ──
    numbers = [2, 8, 15, 3, 21, 7]

    # Without walrus — compute twice or use temp var
    # With walrus — compute once, assign AND test
    results = []
    for n in numbers:
        if (doubled := n * 2) > 10:
            results.append(doubled)
    print(f"    Doubled > 10: {results}")

    # ── In list comprehensions ──
    data = ["Hello", "", "World", "", "Python"]
    non_empty = [upper for s in data if (upper := s.upper())]
    print(f"    Non-empty upper: {non_empty}")


# ═══════════════════════════════════════════════════
# 7. GUARD CLAUSES — Clean Code Pattern
# ═══════════════════════════════════════════════════

def demo_guard_clauses():
    """Early returns to avoid deep nesting."""

    # ❌ Deeply nested
    def process_order_nested(order):
        if order is not None:
            if order.get("items"):
                if order.get("payment"):
                    if order["payment"].get("verified"):
                        return f"Processing {len(order['items'])} items"
        return "Invalid order"

    # ✅ Guard clauses — flat and readable
    def process_order(order):
        if order is None:
            return "Error: No order"
        if not order.get("items"):
            return "Error: No items"
        if not order.get("payment"):
            return "Error: No payment"
        if not order["payment"].get("verified"):
            return "Error: Payment not verified"

        return f"✅ Processing {len(order['items'])} items"

    test_orders = [
        None,
        {},
        {"items": ["book"]},
        {"items": ["book"], "payment": {}},
        {"items": ["book"], "payment": {"verified": True}},
    ]

    for order in test_orders:
        print(f"    {process_order(order)}")


# ═══════════════════════════════════════════════════
# 8. MATCH/CASE — Structural Pattern Matching (3.10+)
# ═══════════════════════════════════════════════════

def demo_pattern_matching():
    """
    Python 3.10+ introduced match/case — far more powerful
    than switch/case in other languages.
    """

    # ── Basic literal matching ──
    def http_status(code: int) -> str:
        match code:
            case 200:
                return "OK"
            case 301:
                return "Moved Permanently"
            case 404:
                return "Not Found"
            case 500:
                return "Internal Server Error"
            case _:
                return f"Unknown ({code})"

    for code in [200, 404, 500, 418]:
        print(f"    HTTP {code}: {http_status(code)}")

    # ── Destructuring sequences ──
    def parse_command(command: list):
        match command:
            case ["quit" | "exit"]:
                return "👋 Goodbye!"
            case ["greet", name]:
                return f"Hello, {name}!"
            case ["move", direction, distance]:
                return f"Moving {direction} by {distance}"
            case ["add", *items]:
                return f"Adding {len(items)} items: {items}"
            case _:
                return f"Unknown command: {command}"

    commands = [
        ["quit"],
        ["greet", "Alice"],
        ["move", "north", "5"],
        ["add", "apple", "banana", "cherry"],
        ["unknown"],
    ]

    print("\n    Command parsing:")
    for cmd in commands:
        print(f"      {cmd!r:40s} → {parse_command(cmd)}")

    # ── Matching dictionaries ──
    def process_event(event: dict):
        match event:
            case {"type": "click", "x": x, "y": y}:
                return f"Click at ({x}, {y})"
            case {"type": "keypress", "key": key}:
                return f"Key pressed: {key}"
            case {"type": "scroll", "direction": d, "amount": a}:
                return f"Scroll {d} by {a}"
            case _:
                return "Unknown event"

    events = [
        {"type": "click", "x": 100, "y": 200},
        {"type": "keypress", "key": "Enter"},
        {"type": "scroll", "direction": "down", "amount": 3},
    ]

    print("\n    Event processing:")
    for event in events:
        print(f"      {process_event(event)}")

    # ── Guard conditions in patterns ──
    def classify_point(point: tuple):
        match point:
            case (0, 0):
                return "Origin"
            case (x, 0):
                return f"X-axis at x={x}"
            case (0, y):
                return f"Y-axis at y={y}"
            case (x, y) if x == y:
                return f"Diagonal at ({x}, {y})"
            case (x, y) if x > 0 and y > 0:
                return f"Quadrant I: ({x}, {y})"
            case (x, y):
                return f"Point ({x}, {y})"

    points = [(0, 0), (5, 0), (0, 3), (4, 4), (2, 7), (-1, -3)]
    print("\n    Point classification:")
    for p in points:
        print(f"      {p} → {classify_point(p)}")


# ─────────────────────────────────────────────────
# DEMO
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    sections = [
        ("1. Basic if/elif/else", demo_basic_conditions),
        ("2. Ternary Expressions", demo_ternary),
        ("3. Chained Comparisons", demo_chained_comparisons),
        ("4. Truthy & Falsy", demo_truthy_falsy),
        ("5. Short-Circuit Evaluation", demo_short_circuit),
        ("6. Walrus Operator :=", demo_walrus),
        ("7. Guard Clauses", demo_guard_clauses),
        ("8. Match/Case (Python 3.10+)", demo_pattern_matching),
    ]
    for title, fn in sections:
        print("\n" + "=" * 55)
        print(title)
        print("=" * 55)
        fn()
