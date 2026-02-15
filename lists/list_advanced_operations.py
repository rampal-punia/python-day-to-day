"""
List Slicing & Advanced Operations — The Pythonic Way
======================================================
Master list slicing, unpacking, sorting, and performance patterns.

Author: @rampal-punia
"""

import copy
import bisect
import sys
from collections import deque


# ═══════════════════════════════════════════════════
# 1. SLICING MASTERY
# ═══════════════════════════════════════════════════
# Syntax: list[start:stop:step]
# - start: inclusive (default 0)
# - stop: exclusive (default len)
# - step: stride (default 1)

def demo_slicing():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(f"    Original         : {nums}")
    print(f"    nums[2:7]        : {nums[2:7]}")         # [2,3,4,5,6]
    print(f"    nums[:5]         : {nums[:5]}")           # [0,1,2,3,4]
    print(f"    nums[5:]         : {nums[5:]}")           # [5,6,7,8,9]
    print(f"    nums[-3:]        : {nums[-3:]}")          # [7,8,9]
    print(f"    nums[:-3]        : {nums[:-3]}")          # [0,1,2,3,4,5,6]
    print(f"    nums[::2]        : {nums[::2]}")          # [0,2,4,6,8]
    print(f"    nums[1::2]       : {nums[1::2]}")         # [1,3,5,7,9]
    print(f"    nums[::-1]       : {nums[::-1]}")         # reversed
    print(f"    nums[::-2]       : {nums[::-2]}")         # [9,7,5,3,1]

    # Named slices — readable alternative
    FIRST_THREE = slice(0, 3)
    LAST_THREE = slice(-3, None)
    EVERY_OTHER = slice(None, None, 2)

    print(f"\n    Named slices:")
    print(f"    FIRST_THREE      : {nums[FIRST_THREE]}")
    print(f"    LAST_THREE       : {nums[LAST_THREE]}")
    print(f"    EVERY_OTHER      : {nums[EVERY_OTHER]}")

    # Slice assignment — replace sections
    data = [0, 1, 2, 3, 4, 5]
    data[1:4] = [10, 20, 30, 40]  # different length is OK!
    print(f"\n    Slice assignment : {data}")

    # Delete via slice
    data[::2] = [None] * len(data[::2])
    print(f"    Replace evens    : {data}")


# ═══════════════════════════════════════════════════
# 2. UNPACKING — Elegant Variable Assignment
# ═══════════════════════════════════════════════════

def demo_unpacking():
    # Basic unpacking
    first, second, third = [10, 20, 30]
    print(f"    Basic: {first}, {second}, {third}")

    # Star unpacking — capture rest
    first, *middle, last = [1, 2, 3, 4, 5]
    print(f"    first={first}, middle={middle}, last={last}")

    head, *_ = [1, 2, 3, 4, 5]  # discard rest
    print(f"    head={head}, rest discarded")

    *_, tail = [1, 2, 3, 4, 5]  # only last
    print(f"    tail={tail}")

    # Swap without temp variable
    a, b = 1, 2
    a, b = b, a
    print(f"    Swapped: a={a}, b={b}")

    # Nested unpacking
    data = [1, [2, 3], 4]
    a, (b, c), d = data
    print(f"    Nested: a={a}, b={b}, c={c}, d={d}")

    # Practical: split head from rest
    def head_tail(lst):
        head, *tail = lst
        return head, tail

    h, t = head_tail([10, 20, 30, 40])
    print(f"    head_tail: head={h}, tail={t}")


# ═══════════════════════════════════════════════════
# 3. SORTING — In-Depth
# ═══════════════════════════════════════════════════

def demo_sorting():
    # sorted() vs .sort()
    original = [3, 1, 4, 1, 5, 9, 2, 6]
    new_sorted = sorted(original)       # returns NEW list
    print(f"    sorted()    : {new_sorted} (original: {original})")

    original.sort()                      # modifies IN PLACE
    print(f"    .sort()     : {original} (modified in place)")

    # Custom key functions
    words = ["banana", "apple", "Cherry", "date"]
    print(f"\n    By length      : {sorted(words, key=len)}")
    print(f"    Case-insensitive: {sorted(words, key=str.lower)}")

    # Sort by multiple criteria
    students = [
        ("Alice", 88), ("Bob", 95), ("Charlie", 88),
        ("Diana", 95), ("Eve", 72),
    ]

    # Sort by score desc, then name asc
    result = sorted(students, key=lambda s: (-s[1], s[0]))
    print(f"\n    Multi-sort (score↓, name↑):")
    for name, score in result:
        print(f"      {name:10s} {score}")

    # Stable sort — preserves relative order of equal elements
    data = [(1, "b"), (2, "a"), (1, "a"), (2, "b")]
    # Sort by first element only — second element stays in insertion order
    stable = sorted(data, key=lambda x: x[0])
    print(f"\n    Stable sort: {stable}")

    # Sort dict by value
    scores = {"Alice": 88, "Bob": 95, "Charlie": 72}
    by_score = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
    print(f"    Dict by value: {by_score}")


# ═══════════════════════════════════════════════════
# 4. BISECT — Sorted List Operations (O(log n))
# ═══════════════════════════════════════════════════

def demo_bisect():
    """bisect module maintains sorted order without re-sorting."""
    sorted_list = [10, 20, 30, 40, 50]

    # Find insertion point
    pos = bisect.bisect(sorted_list, 25)
    print(f"    bisect(25)          : position {pos}")

    # Insert maintaining order
    bisect.insort(sorted_list, 25)
    print(f"    insort(25)          : {sorted_list}")

    bisect.insort(sorted_list, 35)
    print(f"    insort(35)          : {sorted_list}")

    # Practical: Grade assignment with bisect
    def grade(score: float, breakpoints=[60, 70, 80, 90], grades="FDCBA"):
        i = bisect.bisect(breakpoints, score)
        return grades[i]

    scores = [33, 60, 71, 82, 95]
    print(f"\n    Grade assignment:")
    for s in scores:
        print(f"      {s:3d} → {grade(s)}")


# ═══════════════════════════════════════════════════
# 5. COPY — Shallow vs Deep
# ═══════════════════════════════════════════════════

def demo_copy():
    # Shallow copy — top level is independent, nested refs are shared
    original = [[1, 2], [3, 4], [5, 6]]

    shallow = original.copy()    # or list(original) or original[:]
    shallow[0].append(99)        # mutates BOTH! (shared reference)
    shallow.append([7, 8])       # only in shallow

    print(f"    Original after shallow mutation: {original}")
    print(f"    Shallow copy                   : {shallow}")

    # Deep copy — fully independent at all levels
    original2 = [[1, 2], [3, 4]]
    deep = copy.deepcopy(original2)
    deep[0].append(99)           # only in deep copy

    print(f"\n    Original after deep mutation: {original2}")
    print(f"    Deep copy                   : {deep}")


# ═══════════════════════════════════════════════════
# 6. LIST AS STACK & QUEUE
# ═══════════════════════════════════════════════════

def demo_stack_queue():
    # Stack (LIFO) — list works perfectly
    stack = []
    stack.append("task_1")
    stack.append("task_2")
    stack.append("task_3")
    print(f"    Stack: {stack}")
    print(f"    Pop  : {stack.pop()} → {stack}")

    # Queue (FIFO) — use deque, NOT list!
    # list.pop(0) is O(n), deque.popleft() is O(1)
    queue = deque()
    queue.append("request_1")
    queue.append("request_2")
    queue.append("request_3")
    print(f"\n    Queue: {list(queue)}")
    print(f"    Serve: {queue.popleft()} → {list(queue)}")

    # Priority queue with heapq
    import heapq
    tasks = []
    heapq.heappush(tasks, (3, "low priority"))
    heapq.heappush(tasks, (1, "urgent"))
    heapq.heappush(tasks, (2, "medium"))

    print(f"\n    Priority Queue:")
    while tasks:
        priority, task = heapq.heappop(tasks)
        print(f"      [{priority}] {task}")


# ═══════════════════════════════════════════════════
# 7. ZIP — Parallel Iteration
# ═══════════════════════════════════════════════════

def demo_zip():
    names = ["Alice", "Bob", "Charlie"]
    scores = [88, 95, 72]
    grades = ["B+", "A", "C"]

    # Basic zip
    combined = list(zip(names, scores, grades))
    print(f"    zip(3 lists) : {combined}")

    # Unzip (transpose)
    n, s, g = zip(*combined)
    print(f"    Unzipped     : {n}, {s}, {g}")

    # zip_longest — handle unequal lengths
    from itertools import zip_longest
    a = [1, 2, 3]
    b = ["a", "b"]
    result = list(zip_longest(a, b, fillvalue="?"))
    print(f"    zip_longest  : {result}")

    # Create dict from two lists
    keys = ["name", "age", "city"]
    values = ["Alice", 28, "NYC"]
    person = dict(zip(keys, values))
    print(f"    dict(zip)    : {person}")

    # Enumerate is zip under the hood
    # enumerate(x) ≈ zip(range(len(x)), x)
    for i, name in enumerate(names, start=1):
        print(f"      {i}. {name}")


# ═══════════════════════════════════════════════════
# 8. PERFORMANCE TIPS
# ═══════════════════════════════════════════════════

def demo_performance():
    N = 100_000

    # List comprehension vs loop
    import time

    start = time.perf_counter()
    result = [x**2 for x in range(N)]
    comp_time = time.perf_counter() - start

    start = time.perf_counter()
    result = []
    for x in range(N):
        result.append(x**2)
    loop_time = time.perf_counter() - start

    print(f"    Comprehension : {comp_time:.4f}s")
    print(f"    For loop      : {loop_time:.4f}s")
    print(f"    Speedup       : {loop_time/comp_time:.1f}x")

    # Membership testing: list vs set
    data_list = list(range(N))
    data_set = set(range(N))

    start = time.perf_counter()
    _ = 99_999 in data_list
    list_time = time.perf_counter() - start

    start = time.perf_counter()
    _ = 99_999 in data_set
    set_time = time.perf_counter() - start

    print(f"\n    Membership test ({N:,}):")
    print(f"    list 'in'     : {list_time:.6f}s")
    print(f"    set 'in'      : {set_time:.6f}s")

    # Memory: list vs generator
    list_mem = sys.getsizeof([x for x in range(N)])
    gen_mem = sys.getsizeof(x for x in range(N))
    print(f"\n    Memory ({N:,} ints):")
    print(f"    List      : {list_mem:>10,} bytes")
    print(f"    Generator : {gen_mem:>10,} bytes")


# ─────────────────────────────────────────────────
# DEMO
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    sections = [
        ("1. Slicing Mastery", demo_slicing),
        ("2. Unpacking Patterns", demo_unpacking),
        ("3. Sorting In-Depth", demo_sorting),
        ("4. Bisect — Sorted Operations", demo_bisect),
        ("5. Shallow vs Deep Copy", demo_copy),
        ("6. Stack, Queue & Priority Queue", demo_stack_queue),
        ("7. Zip — Parallel Iteration", demo_zip),
        ("8. Performance Tips", demo_performance),
    ]
    for title, fn in sections:
        print("\n" + "=" * 55)
        print(title)
        print("=" * 55)
        fn()
