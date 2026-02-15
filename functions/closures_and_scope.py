"""
Closures & Scope — LEGB Rule Demystified
==========================================
Understanding variable scope and closures in Python.

Author: @rampal-punia
"""

# ═══════════════════════════════════════════════════
# THE LEGB RULE — Variable Lookup Order
# ═══════════════════════════════════════════════════
#
#   L — Local      : Variables inside the current function
#   E — Enclosing  : Variables in enclosing (outer) function
#   G — Global     : Variables at module level
#   B — Built-in   : Python's built-in names (len, print, etc.)
#
# Python searches in this order: L → E → G → B


# ─────────────────────────────────────────────────
# 1. SCOPE LEVELS DEMONSTRATED
# ─────────────────────────────────────────────────

x = "Global"  # Global scope


def outer():
    x = "Enclosing"  # Enclosing scope

    def inner():
        x = "Local"  # Local scope
        print(f"  inner() sees: {x}")  # → Local

    inner()
    print(f"  outer() sees: {x}")  # → Enclosing


# ─────────────────────────────────────────────────
# 2. global AND nonlocal KEYWORDS
# ─────────────────────────────────────────────────

counter = 0  # Global


def increment_global():
    """Modify a global variable from inside a function."""
    global counter
    counter += 1
    print(f"  Global counter: {counter}")


def make_counter():
    """Modify an enclosing variable using nonlocal."""
    count = 0

    def increment():
        nonlocal count  # refers to enclosing 'count'
        count += 1
        return count

    return increment


# ─────────────────────────────────────────────────
# 3. CLOSURES — Functions That Remember
# ─────────────────────────────────────────────────


def make_multiplier(factor: int):
    """
    A closure captures 'factor' from the enclosing scope.
    Even after make_multiplier returns, the inner function
    still has access to 'factor'.
    """

    def multiplier(x: int) -> int:
        return x * factor  # 'factor' is a free variable

    return multiplier


# ─────────────────────────────────────────────────
# 4. PRACTICAL CLOSURE — Configurable Logger
# ─────────────────────────────────────────────────


def create_logger(prefix: str, separator: str = " | "):
    """Create a logger function with a configurable prefix."""
    import datetime

    def log(message: str):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"  [{timestamp}]{separator}{prefix}{separator}{message}")

    return log


# ─────────────────────────────────────────────────
# 5. CLOSURE FOR DATA ENCAPSULATION (Private State)
# ─────────────────────────────────────────────────


def create_bank_account(owner: str, initial_balance: float = 0):
    """
    Closure as a lightweight object — private state without classes.
    The balance is truly private, not accessible from outside.
    """
    balance = initial_balance

    def deposit(amount: float) -> float:
        nonlocal balance
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        balance += amount
        return balance

    def withdraw(amount: float) -> float:
        nonlocal balance
        if amount > balance:
            raise ValueError(f"Insufficient funds: ${balance:.2f}")
        balance -= amount
        return balance

    def get_balance() -> float:
        return balance

    def statement() -> str:
        return f"  💳 {owner}'s account: ${balance:.2f}"

    # Return a dict of operations (poor-man's object)
    return {
        "deposit": deposit,
        "withdraw": withdraw,
        "balance": get_balance,
        "statement": statement,
    }


# ─────────────────────────────────────────────────
# 6. COMMON GOTCHA — Late Binding in Loops
# ─────────────────────────────────────────────────


def late_binding_problem():
    """All lambdas capture the SAME variable `i` by reference."""
    functions = []
    for i in range(5):
        functions.append(lambda: i)  # ❌ All reference same `i`

    # All return 4 (the final value of i)!
    results = [f() for f in functions]
    print(f"  ❌ Late binding : {results}")  # [4, 4, 4, 4, 4]


def late_binding_fix():
    """Fix: Use default argument to capture current value."""
    functions = []
    for i in range(5):
        functions.append(lambda i=i: i)  # ✅ Default captures current value

    results = [f() for f in functions]
    print(f"  ✅ Default arg  : {results}")  # [0, 1, 2, 3, 4]


# ─────────────────────────────────────────────────
# 7. INSPECTING CLOSURES
# ─────────────────────────────────────────────────


def inspect_closure():
    """You can inspect a closure's captured variables."""
    double = make_multiplier(2)

    print(f"  Function name   : {double.__name__}")
    print(f"  Free variables  : {double.__code__.co_freevars}")

    if double.__closure__:
        for cell in double.__closure__:
            print(f"  Captured value  : {cell.cell_contents}")


# ─────────────────────────────────────────────────
# DEMO
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("1. LEGB Scope Levels")
    print("=" * 55)
    outer()
    print(f"  module sees : {x}")

    print("\n" + "=" * 55)
    print("2. global & nonlocal Keywords")
    print("=" * 55)
    increment_global()
    increment_global()

    counter_fn = make_counter()
    print(f"  nonlocal counter: {counter_fn()}")  # 1
    print(f"  nonlocal counter: {counter_fn()}")  # 2
    print(f"  nonlocal counter: {counter_fn()}")  # 3

    print("\n" + "=" * 55)
    print("3. Closures — Functions That Remember")
    print("=" * 55)
    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(f"  double(5) = {double(5)}")  # 10
    print(f"  triple(5) = {triple(5)}")  # 15

    print("\n" + "=" * 55)
    print("4. Configurable Logger Closure")
    print("=" * 55)
    info_log = create_logger("INFO")
    error_log = create_logger("ERROR", " ⚠️ ")
    info_log("Application started")
    error_log("Something went wrong")

    print("\n" + "=" * 55)
    print("5. Bank Account — Private State via Closure")
    print("=" * 55)
    account = create_bank_account("Alice", 100.0)
    account["deposit"](50)
    account["withdraw"](30)
    print(account["statement"]())

    print("\n" + "=" * 55)
    print("6. Late Binding Gotcha & Fix")
    print("=" * 55)
    late_binding_problem()
    late_binding_fix()

    print("\n" + "=" * 55)
    print("7. Inspecting Closures")
    print("=" * 55)
    inspect_closure()
