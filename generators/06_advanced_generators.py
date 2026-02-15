"""
Advanced Generators — yield from, send(), and Real-World Pipelines
===================================================================
Taking generators beyond basics into production patterns.

Author: @rampal-punia
"""

import os
import sys
import itertools
from pathlib import Path
from typing import Generator, Iterator


# ═══════════════════════════════════════════════════
# 1. yield from — Delegating to Sub-Generators
# ═══════════════════════════════════════════════════

def flatten_recursive(nested):
    """
    Flatten arbitrarily nested iterables using 'yield from'.
    yield from = delegate to another generator/iterable.
    """
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten_recursive(item)  # delegate!
        else:
            yield item


def chain_generators(*generators):
    """Combine multiple generators into one (like itertools.chain)."""
    for gen in generators:
        yield from gen  # much cleaner than: for item in gen: yield item


def demo_yield_from():
    nested = [1, [2, 3, [4, 5]], 6, [7, [8, [9]]]]
    flat = list(flatten_recursive(nested))
    print(f"    Flattened: {flat}")

    # Chain generators together
    evens = (x for x in range(0, 6, 2))
    odds = (x for x in range(1, 6, 2))
    combined = list(chain_generators(evens, odds))
    print(f"    Chained  : {combined}")


# ═══════════════════════════════════════════════════
# 2. send() — Two-Way Communication with Generators
# ═══════════════════════════════════════════════════

def running_average() -> Generator[float, float, None]:
    """
    A generator that maintains a running average.
    Values are sent IN, averages are yielded OUT.
    """
    total = 0.0
    count = 0
    average = 0.0

    while True:
        value = yield average  # yield current average, receive new value
        if value is None:
            break
        total += value
        count += 1
        average = total / count


def accumulator(initial: int = 0) -> Generator[int, int, str]:
    """
    Accumulates values sent to it.
    Demonstrates send() and return value via StopIteration.
    """
    total = initial
    while True:
        received = yield total
        if received is None:
            break
        total += received
    return f"Final total: {total}"  # captured via StopIteration


def demo_send():
    # Running average
    avg = running_average()
    next(avg)  # Prime the generator (advance to first yield)

    values = [10, 20, 30, 40, 50]
    print("    Running average:")
    for v in values:
        current_avg = avg.send(v)
        print(f"      Added {v:3d} → avg = {current_avg:.1f}")

    # Accumulator with return value
    acc = accumulator(100)
    next(acc)  # prime

    for v in [5, 10, 15]:
        result = acc.send(v)
        print(f"    Accumulated: {result}")

    try:
        acc.send(None)  # trigger return
    except StopIteration as e:
        print(f"    {e.value}")  # "Final total: 130"


# ═══════════════════════════════════════════════════
# 3. throw() and close() — Error Handling
# ═══════════════════════════════════════════════════

def supervised_generator():
    """A generator that handles exceptions sent to it."""
    while True:
        try:
            value = yield
            print(f"    Processed: {value}")
        except ValueError as e:
            print(f"    ⚠️  Handled error: {e}")
        except GeneratorExit:
            print("    🛑 Generator closed gracefully")
            return


def demo_throw_close():
    gen = supervised_generator()
    next(gen)  # prime

    gen.send("data_1")
    gen.send("data_2")
    gen.throw(ValueError, "Bad data!")  # generator handles it
    gen.send("data_3")
    gen.close()  # triggers GeneratorExit


# ═══════════════════════════════════════════════════
# 4. GENERATOR EXPRESSIONS vs FUNCTIONS
# ═══════════════════════════════════════════════════

def demo_expressions_vs_functions():
    """When to use which."""

    # Generator expression — for simple transforms
    squares_expr = (x**2 for x in range(10))  # no [] brackets!
    print(f"    Expression type  : {type(squares_expr)}")
    print(f"    First 5 squares  : {[next(squares_expr) for _ in range(5)]}")

    # Memory comparison
    list_size = sys.getsizeof([x**2 for x in range(10_000)])
    gen_size = sys.getsizeof(x**2 for x in range(10_000))
    print(f"\n    Memory for 10K squares:")
    print(f"      List       : {list_size:>8,} bytes")
    print(f"      Generator  : {gen_size:>8,} bytes")
    print(f"      Savings    : {list_size/gen_size:.0f}x less memory 🚀")

    # Pass generator expression directly to functions
    total = sum(x**2 for x in range(100))  # no extra parentheses needed
    has_even = any(x % 2 == 0 for x in [1, 3, 4, 7])
    max_len = max(len(w) for w in ["hello", "magnificent", "hi"])
    print(f"\n    sum(x² for x<100) = {total}")
    print(f"    any even?          = {has_even}")
    print(f"    max word length    = {max_len}")


# ═══════════════════════════════════════════════════
# 5. REAL-WORLD: ETL PIPELINE
# ═══════════════════════════════════════════════════

def demo_etl_pipeline():
    """
    Extract → Transform → Load pipeline using generators.
    Each stage processes one item at a time — memory efficient.
    """

    # Simulated raw data (Extract)
    raw_records = [
        "Alice,28,85000,engineering",
        "Bob,35,92000,marketing",
        "CHARLIE,42,78000,ENGINEERING",
        "Diana,31,105000,Engineering",
        "Eve,26,,design",           # missing salary
        "Frank,29,88000,marketing",
    ]

    # Stage 1: Parse CSV lines (Extract)
    def parse_records(lines):
        for line in lines:
            parts = line.split(",")
            if len(parts) == 4:
                yield {
                    "name": parts[0],
                    "age": parts[1],
                    "salary": parts[2],
                    "dept": parts[3],
                }

    # Stage 2: Clean & normalize (Transform)
    def normalize(records):
        for r in records:
            yield {
                "name": r["name"].title(),
                "age": int(r["age"]),
                "salary": float(r["salary"]) if r["salary"] else 0.0,
                "dept": r["dept"].lower(),
            }

    # Stage 3: Filter valid records (Transform)
    def filter_valid(records):
        for r in records:
            if r["salary"] > 0:
                yield r

    # Stage 4: Enrich with tax calculation (Transform)
    def add_tax(records, rate=0.3):
        for r in records:
            r["tax"] = round(r["salary"] * rate, 2)
            r["net"] = round(r["salary"] - r["tax"], 2)
            yield r

    # Pipeline composition — each stage is lazy!
    pipeline = add_tax(
        filter_valid(
            normalize(
                parse_records(raw_records)
            )
        )
    )

    # Stage 5: Consume (Load)
    print("    ETL Pipeline Results:")
    print(f"    {'Name':10s} {'Age':>4s} {'Salary':>10s} {'Tax':>10s} {'Net':>10s} {'Dept'}")
    print("    " + "-" * 60)
    for record in pipeline:
        print(
            f"    {record['name']:10s} {record['age']:4d} "
            f"${record['salary']:>9,.0f} ${record['tax']:>9,.0f} "
            f"${record['net']:>9,.0f} {record['dept']}"
        )


# ═══════════════════════════════════════════════════
# 6. ITERTOOLS + GENERATORS — Power Combo
# ═══════════════════════════════════════════════════

def demo_itertools_combo():
    """Essential itertools that pair beautifully with generators."""

    # islice — take N items from infinite generator
    def fibonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    first_10 = list(itertools.islice(fibonacci(), 10))
    print(f"    First 10 Fibonacci: {first_10}")

    # takewhile / dropwhile — conditional slicing
    nums = [2, 4, 6, 7, 8, 10, 1, 3]
    evens = list(itertools.takewhile(lambda x: x % 2 == 0, nums))
    print(f"    takewhile(even)   : {evens}")  # stops at 7

    # groupby — group consecutive equal elements
    data = "AAABBBCCAAB"
    groups = [(k, list(g)) for k, g in itertools.groupby(data)]
    print(f"    groupby           : {groups}")

    # chain.from_iterable — flatten one level
    nested = [[1, 2], [3, 4], [5, 6]]
    flat = list(itertools.chain.from_iterable(nested))
    print(f"    chain.from_iter   : {flat}")

    # product — cartesian product
    colors = ["R", "G"]
    sizes = ["S", "M", "L"]
    combos = list(itertools.product(colors, sizes))
    print(f"    product           : {combos}")

    # accumulate — running totals
    nums = [1, 2, 3, 4, 5]
    running = list(itertools.accumulate(nums))
    print(f"    accumulate(sum)   : {running}")

    # batched (Python 3.12+) or manual
    def batched(iterable, n):
        """Batch items into groups of n."""
        it = iter(iterable)
        while batch := list(itertools.islice(it, n)):
            yield batch

    data = list(range(1, 11))
    batches = list(batched(data, 3))
    print(f"    batched(3)        : {batches}")


# ─────────────────────────────────────────────────
# DEMO
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    sections = [
        ("1. yield from — Delegation", demo_yield_from),
        ("2. send() — Two-Way Communication", demo_send),
        ("3. throw() & close() — Error Handling", demo_throw_close),
        ("4. Expressions vs Functions", demo_expressions_vs_functions),
        ("5. Real-World ETL Pipeline", demo_etl_pipeline),
        ("6. itertools + Generators", demo_itertools_combo),
    ]
    for title, fn in sections:
        print("\n" + "=" * 55)
        print(title)
        print("=" * 55)
        fn()
