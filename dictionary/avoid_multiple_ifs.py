"""Avoid Multiple if-else — Use dictionaries for cleaner dispatch.

Difficulty: 🟢 Easy → 🟡 Intermediate
Topics: dict.get(), dispatch tables, ordinal suffixes, strategy pattern

Instead of long if/elif/else chains, map inputs to outputs using a dict.
This is cleaner, faster (O(1) lookup), and easier to extend.

Author: @rampal-punia
"""

# ── 🟢 Easy: Ordinal Suffix with dict.get() ──


def ordinal(n: int) -> str:
    """Return the ordinal string for an integer (e.g., 1 → '1st', 22 → '22nd').

    Handles all edge cases including 11th, 12th, 13th.

    Args:
        n: A positive integer.

    Returns:
        The ordinal string (e.g., '1st', '2nd', '3rd', '4th', '11th', '21st').
    """
    suffix_map = {1: "st", 2: "nd", 3: "rd"}
    # 11, 12, 13 are exceptions — they use 'th' not 'st/nd/rd'
    if 11 <= n % 100 <= 13:
        return f"{n}th"
    return f"{n}{suffix_map.get(n % 10, 'th')}"


# ── 🟡 Intermediate: Dict-Based Dispatch (replacing if/elif chains) ──


def http_status_message(code: int) -> str:
    """Map HTTP status codes to messages using a dictionary.

    Without dict: 10+ lines of if/elif. With dict: 1 lookup.
    """
    status_messages = {
        200: "OK",
        201: "Created",
        301: "Moved Permanently",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        500: "Internal Server Error",
    }
    return status_messages.get(code, f"Unknown Status ({code})")


# ── 🟡 Intermediate: Function Dispatch Table ──


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


OPERATIONS: dict[str, callable] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(a: float, op: str, b: float) -> float:
    """Perform a calculation using a dispatch table instead of if/elif."""
    func = OPERATIONS.get(op)
    if func is None:
        raise ValueError(f"Unknown operator: {op!r}")
    return func(a, b)


if __name__ == "__main__":
    # ── Ordinal suffixes ──
    print("── Ordinal Suffixes ──")
    test_numbers = [1, 2, 3, 4, 11, 12, 13, 21, 22, 23, 101, 111, 112, 113]
    for n in test_numbers:
        print(f"  {n:>4} → {ordinal(n)}")

    # ── HTTP status lookup ──
    print("\n── HTTP Status Messages ──")
    for code in [200, 404, 500, 999]:
        print(f"  {code} → {http_status_message(code)}")

    # ── Calculator dispatch ──
    print("\n── Calculator Dispatch Table ──")
    examples = [(10, "+", 5), (10, "-", 3), (4, "*", 7), (20, "/", 4)]
    for a, op, b in examples:
        print(f"  {a} {op} {b} = {calculate(a, op, b)}")

# For more on Python follow: https://x.com/rs_punia_
