"""
functools Module — Essential Tools for Functional Programming
=============================================================
The functools module provides higher-order functions and operations
on callable objects. These are production-grade utilities.

Author: @rampal-punia
"""

import functools
import time
import operator
from typing import Callable


# ─────────────────────────────────────────────────
# 1. functools.lru_cache — Automatic Memoization
# ─────────────────────────────────────────────────


@functools.lru_cache(maxsize=256)
def expensive_computation(n: int) -> int:
    """Fibonacci with built-in caching. O(n) instead of O(2^n)."""
    if n < 2:
        return n
    return expensive_computation(n - 1) + expensive_computation(n - 2)


def demo_lru_cache():
    print(f"  fib(50)    = {expensive_computation(50)}")

    # Inspect cache statistics
    info = expensive_computation.cache_info()
    print(f"  Cache info = {info}")
    # CacheInfo(hits=48, misses=51, maxsize=256, currsize=51)


# ─────────────────────────────────────────────────
# 2. functools.partial — Pre-fill Function Arguments
# ─────────────────────────────────────────────────


def demo_partial():
    """Create specialized functions from general ones."""

    # Create specialized power functions
    square = functools.partial(pow, exp=2)
    cube = functools.partial(pow, exp=3)

    # Create a base-2 logger
    log2 = functools.partial(int, base=2)

    # Create a custom print
    debug_print = functools.partial(print, "[DEBUG]", sep=" | ", end="\n\n")

    print(f"  square(5) = {pow(5, exp=2)}")
    print(f"  cube(3)   = {pow(3, exp=3)}")
    print(f"  log2('1010') = {log2('1010')}")  # 10
    debug_print("Server started", "Port: 8080")


# ─────────────────────────────────────────────────
# 3. functools.reduce — Aggregate to Single Value
# ─────────────────────────────────────────────────


def demo_reduce():
    """Reduce examples with operator module integration."""
    numbers = [1, 2, 3, 4, 5]

    # Sum using operator.add
    total = functools.reduce(operator.add, numbers)
    print(f"  Sum     : {total}")

    # Product using operator.mul
    product = functools.reduce(operator.mul, numbers)
    print(f"  Product : {product}")

    # Find max using operator
    maximum = functools.reduce(max, numbers)
    print(f"  Max     : {maximum}")

    # Flatten deeply nested structure
    nested = [[1, 2], [3, [4, 5]], [6]]
    flat = functools.reduce(operator.concat, [[1, 2], [3, 4], [5, 6]])
    print(f"  Flat    : {flat}")


# ─────────────────────────────────────────────────
# 4. functools.wraps — Preserve Function Metadata
# ─────────────────────────────────────────────────


def without_wraps(func):
    """❌ Without @wraps — loses original function metadata."""

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def with_wraps(func):
    """✅ With @wraps — preserves original function metadata."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@without_wraps
def greet_bad(name: str) -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"


@with_wraps
def greet_good(name: str) -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"


def demo_wraps():
    print(f"  Without @wraps:")
    print(f"    __name__ = {greet_bad.__name__}")  # 'wrapper' ❌
    print(f"    __doc__  = {greet_bad.__doc__}")  # None ❌

    print(f"  With @wraps:")
    print(f"    __name__ = {greet_good.__name__}")  # 'greet_good' ✅
    print(f"    __doc__  = {greet_good.__doc__}")  # 'Say hello...' ✅


# ─────────────────────────────────────────────────
# 5. functools.total_ordering — Auto-generate Comparisons
# ─────────────────────────────────────────────────


@functools.total_ordering
class Student:
    """Only define __eq__ and __lt__, get all 6 comparisons free."""

    def __init__(self, name: str, grade: float):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade

    def __repr__(self):
        return f"Student({self.name!r}, {self.grade})"


def demo_total_ordering():
    alice = Student("Alice", 88)
    bob = Student("Bob", 92)

    print(f"  {alice} < {bob}  : {alice < bob}")  # True
    print(f"  {alice} > {bob}  : {alice > bob}")  # False
    print(f"  {alice} <= {bob} : {alice <= bob}")  # True
    print(f"  {alice} >= {bob} : {alice >= bob}")  # False
    print(f"  {alice} == {bob} : {alice == bob}")  # False


# ─────────────────────────────────────────────────
# 6. functools.singledispatch — Type-Based Dispatch
# ─────────────────────────────────────────────────


@functools.singledispatch
def format_value(value) -> str:
    """Default handler for unknown types."""
    return f"Object: {value!r}"


@format_value.register(int)
def _(value: int) -> str:
    return f"Integer: {value:,}"


@format_value.register(float)
def _(value: float) -> str:
    return f"Float: {value:.4f}"


@format_value.register(list)
def _(value: list) -> str:
    return f"List[{len(value)} items]: {value}"


@format_value.register(dict)
def _(value: dict) -> str:
    return f"Dict[{len(value)} keys]: {list(value.keys())}"


def demo_singledispatch():
    """Different behavior based on argument type — no if/elif needed."""
    values = [42, 3.14159, [1, 2, 3], {"a": 1, "b": 2}, "hello"]
    for v in values:
        print(f"  {format_value(v)}")


# ─────────────────────────────────────────────────
# 7. functools.cached_property — Python 3.8+
# ─────────────────────────────────────────────────


class DataAnalyzer:
    """cached_property computes only once, then caches the result."""

    def __init__(self, data: list):
        self.data = data

    @functools.cached_property
    def stats(self) -> dict:
        """Expensive computation — runs only once."""
        print("    💤 Computing stats (only happens once)...")
        return {
            "count": len(self.data),
            "sum": sum(self.data),
            "mean": sum(self.data) / len(self.data),
            "min": min(self.data),
            "max": max(self.data),
        }


def demo_cached_property():
    analyzer = DataAnalyzer([10, 20, 30, 40, 50])
    print(f"  First access : {analyzer.stats}")  # computes
    print(f"  Second access: {analyzer.stats}")  # cached!


# ─────────────────────────────────────────────────
# DEMO
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    sections = [
        ("1. lru_cache — Memoization", demo_lru_cache),
        ("2. partial — Pre-fill Arguments", demo_partial),
        ("3. reduce — Aggregate Values", demo_reduce),
        ("4. wraps — Preserve Metadata", demo_wraps),
        ("5. total_ordering — Auto Comparisons", demo_total_ordering),
        ("6. singledispatch — Type-Based Dispatch", demo_singledispatch),
        ("7. cached_property — Lazy Computation", demo_cached_property),
    ]

    for title, demo_fn in sections:
        print("=" * 55)
        print(title)
        print("=" * 55)
        demo_fn()
        print()
