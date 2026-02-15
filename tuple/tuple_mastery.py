"""
Tuple Mastery — Immutability, Unpacking & Advanced Patterns
=============================================================
Everything you need to know about Python tuples.

Author: @rampal-punia
"""

import sys
from collections import namedtuple
from typing import NamedTuple


# ═══════════════════════════════════════════════════
# 1. TUPLE FUNDAMENTALS — Immutability & Hashability
# ═══════════════════════════════════════════════════

def demo_fundamentals():
    # Creation
    t1 = (1, 2, 3)               # parentheses
    t2 = 1, 2, 3                 # comma creates tuple (not parentheses!)
    t3 = tuple([1, 2, 3])        # from iterable
    t4 = (42,)                   # single element — comma is required!
    t5 = ()                      # empty tuple
    t6 = tuple()                 # empty tuple (alternative)

    # ⚠️ Common gotcha
    not_a_tuple = (42)           # this is just int 42!
    is_a_tuple = (42,)           # THIS is a tuple

    print(f"    (42)  → type: {type(not_a_tuple).__name__}, value: {not_a_tuple}")
    print(f"    (42,) → type: {type(is_a_tuple).__name__}, value: {is_a_tuple}")

    # Immutability
    t = (1, 2, 3)
    try:
        t[0] = 99  # TypeError!
    except TypeError as e:
        print(f"\n    Immutable: {e}")

    # ⚠️ But mutable contents CAN be modified!
    t = ([1, 2], [3, 4])
    t[0].append(99)  # This works!
    print(f"    Mutable contents: {t}")  # ([1, 2, 99], [3, 4])

    # Hashability — only if ALL elements are hashable
    hashable = (1, 2, "hello")
    print(f"\n    hash((1,2,'hello')) = {hash(hashable)}")

    unhashable = (1, [2, 3])
    try:
        hash(unhashable)
    except TypeError as e:
        print(f"    hash((1,[2,3]))    = ❌ {e}")


# ═══════════════════════════════════════════════════
# 2. TUPLE UNPACKING — The Pythonic Superpower
# ═══════════════════════════════════════════════════

def demo_unpacking():
    # Basic unpacking
    point = (10, 20, 30)
    x, y, z = point
    print(f"    x={x}, y={y}, z={z}")

    # Swap values — tuple unpacking magic
    a, b = 1, 2
    a, b = b, a
    print(f"    Swapped: a={a}, b={b}")

    # Star unpacking
    first, *rest = (1, 2, 3, 4, 5)
    print(f"    first={first}, rest={rest}")

    *init, last = (1, 2, 3, 4, 5)
    print(f"    init={init}, last={last}")

    first, *middle, last = (1, 2, 3, 4, 5)
    print(f"    first={first}, middle={middle}, last={last}")

    # Nested unpacking
    data = ("Alice", (2026, 2, 15), "NYC")
    name, (year, month, day), city = data
    print(f"\n    Nested: {name} born {year}-{month:02d}-{day:02d} in {city}")

    # Ignore values with _
    _, important, _ = (1, 42, 3)
    print(f"    Ignoring: important = {important}")

    # Multiple return values (actually returns tuple!)
    def get_stats(numbers):
        return min(numbers), max(numbers), sum(numbers) / len(numbers)

    low, high, avg = get_stats([10, 20, 30, 40, 50])
    print(f"\n    Stats: min={low}, max={high}, avg={avg}")


# ═══════════════════════════════════════════════════
# 3. TUPLES AS DICT KEYS — Immutable Advantage
# ═══════════════════════════════════════════════════

def demo_as_dict_keys():
    """Lists can't be dict keys (unhashable), but tuples can!"""

    # Grid/sparse matrix using tuple keys
    grid = {}
    grid[(0, 0)] = "start"
    grid[(1, 0)] = "wall"
    grid[(0, 1)] = "path"
    grid[(1, 1)] = "goal"

    print("    Grid with tuple keys:")
    for pos, label in grid.items():
        print(f"      {pos} → {label}")

    # Caching with tuple keys
    cache = {}
    def fibonacci(n, memo=cache):
        if n < 2:
            return n
        key = (n,)  # tuple as cache key
        if key not in memo:
            memo[key] = fibonacci(n - 1) + fibonacci(n - 2)
        return memo[key]

    print(f"\n    fib(10) = {fibonacci(10)}")

    # Multi-dimensional lookup
    translation = {
        ("en", "hello"): "hello",
        ("es", "hello"): "hola",
        ("fr", "hello"): "bonjour",
        ("de", "hello"): "hallo",
    }
    for (lang, _), word in translation.items():
        print(f"      {lang}: {word}")


# ═══════════════════════════════════════════════════
# 4. TUPLE METHODS & OPERATIONS
# ═══════════════════════════════════════════════════

def demo_methods():
    t = (1, 2, 3, 2, 4, 2, 5)

    # Only two methods! (because immutable)
    print(f"    count(2)   : {t.count(2)}")    # 3
    print(f"    index(4)   : {t.index(4)}")    # 4

    # Concatenation (creates new tuple)
    t1 = (1, 2)
    t2 = (3, 4)
    t3 = t1 + t2
    print(f"    (1,2) + (3,4) = {t3}")

    # Repetition
    t4 = (0,) * 5
    print(f"    (0,) * 5      = {t4}")

    # Membership
    print(f"    3 in (1,2,3)  = {3 in (1, 2, 3)}")

    # Comparison (lexicographic)
    print(f"    (1,2) < (1,3) = {(1, 2) < (1, 3)}")  # True
    print(f"    (1,2) < (2,0) = {(1, 2) < (2, 0)}")  # True
    print(f"    (1,2) == (1,2) = {(1, 2) == (1, 2)}") # True


# ═══════════════════════════════════════════════════
# 5. NAMED TUPLES — Self-Documenting Tuples
# ═══════════════════════════════════════════════════

def demo_named_tuples():
    # Classic namedtuple
    Point = namedtuple("Point", ["x", "y", "z"])
    p = Point(1, 2, 3)
    print(f"    namedtuple Point: {p}")
    print(f"    p.x={p.x}, p.y={p.y}, p.z={p.z}")

    # typing.NamedTuple (modern, with types)
    class Employee(NamedTuple):
        name: str
        department: str
        salary: float
        is_remote: bool = False  # default value

    emp = Employee("Alice", "Engineering", 95_000, True)
    print(f"\n    NamedTuple: {emp}")
    print(f"    Name: {emp.name}, Remote: {emp.is_remote}")

    # Convert to dict
    print(f"    _asdict(): {emp._asdict()}")

    # Create from iterable
    data = ["Bob", "Marketing", 85_000]
    emp2 = Employee._make(data + [False])
    print(f"    _make(): {emp2}")

    # Replace (returns new instance)
    emp3 = emp._replace(salary=100_000)
    print(f"    _replace(): {emp3}")

    # Still a tuple — can unpack
    name, dept, salary, remote = emp
    print(f"    Unpacked: {name} in {dept}")


# ═══════════════════════════════════════════════════
# 6. TUPLE vs LIST — When to Use Which
# ═══════════════════════════════════════════════════

def demo_tuple_vs_list():
    """
    ┌─────────────┬──────────────────┬──────────────────┐
    │ Feature     │ Tuple            │ List             │
    ├─────────────┼──────────────────┼──────────────────┤
    │ Mutability  │ Immutable ❄️     │ Mutable 🔄       │
    │ Hashable    │ Yes (if elems)   │ No               │
    │ Dict key    │ Yes ✅           │ No ❌            │
    │ Performance │ Faster 🚀       │ Slower           │
    │ Memory      │ Less 📦          │ More             │
    │ Use case    │ Fixed records    │ Dynamic collect. │
    │ Syntax      │ ()               │ []               │
    └─────────────┴──────────────────┴──────────────────┘
    """
    # Memory comparison
    lst = [1, 2, 3, 4, 5]
    tpl = (1, 2, 3, 4, 5)

    print(f"    Memory — list: {sys.getsizeof(lst)} bytes")
    print(f"    Memory — tuple: {sys.getsizeof(tpl)} bytes")
    print(f"    Savings: {sys.getsizeof(lst) - sys.getsizeof(tpl)} bytes")

    # Speed comparison
    import timeit

    list_time = timeit.timeit("[1,2,3,4,5]", number=1_000_000)
    tuple_time = timeit.timeit("(1,2,3,4,5)", number=1_000_000)

    print(f"\n    Create 1M times:")
    print(f"    List  : {list_time:.4f}s")
    print(f"    Tuple : {tuple_time:.4f}s")
    print(f"    Tuple is {list_time/tuple_time:.1f}x faster")

    # Use tuples for:
    print("\n    ✅ Use TUPLE for:")
    print("      • Function return values")
    print("      • Dictionary keys")
    print("      • Immutable records (coordinates, RGB)")
    print("      • Constants / config values")

    print("\n    ✅ Use LIST for:")
    print("      • Collections that grow/shrink")
    print("      • When you need .sort(), .append(), etc.")
    print("      • Homogeneous sequences")


# ═══════════════════════════════════════════════════
# 7. TUPLE COMPREHENSION? — No, It's a Generator!
# ═══════════════════════════════════════════════════

def demo_comprehension_gotcha():
    """() comprehension creates a GENERATOR, not a tuple!"""

    # This is NOT a tuple comprehension
    gen = (x**2 for x in range(5))
    print(f"    (x² for x) type: {type(gen).__name__}")  # generator

    # To create a tuple, wrap in tuple()
    tpl = tuple(x**2 for x in range(5))
    print(f"    tuple(x² for x): {tpl}")

    # Or use * unpacking inside tuple literal
    tpl2 = (*range(5),)  # unpack into tuple
    print(f"    (*range(5),)   : {tpl2}")


# ─────────────────────────────────────────────────
# DEMO
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    sections = [
        ("1. Fundamentals — Immutability", demo_fundamentals),
        ("2. Unpacking — The Superpower", demo_unpacking),
        ("3. Tuples as Dict Keys", demo_as_dict_keys),
        ("4. Methods & Operations", demo_methods),
        ("5. Named Tuples", demo_named_tuples),
        ("6. Tuple vs List", demo_tuple_vs_list),
        ("7. Comprehension Gotcha", demo_comprehension_gotcha),
    ]
    for title, fn in sections:
        print("\n" + "=" * 55)
        print(title)
        print("=" * 55)
        fn()
