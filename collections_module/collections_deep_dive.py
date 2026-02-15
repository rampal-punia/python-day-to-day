"""
collections Module — Essential Data Structures
================================================
deque, defaultdict, Counter, ChainMap, OrderedDict — with real-world examples.

Author: @rampal-punia
"""

from collections import (
    deque, defaultdict, Counter, ChainMap,
    OrderedDict, namedtuple
)
import time


# ═══════════════════════════════════════════════════
# 1. DEQUE — Double-Ended Queue (O(1) both ends)
# ═══════════════════════════════════════════════════

def demo_deque():
    """deque is far superior to list for append/pop at both ends."""

    # Basic operations
    d = deque([1, 2, 3, 4, 5])
    print(f"    Initial        : {d}")

    d.appendleft(0)          # O(1) — list.insert(0, x) is O(n)!
    d.append(6)
    print(f"    After appends  : {d}")

    d.popleft()              # O(1) — list.pop(0) is O(n)!
    d.pop()
    print(f"    After pops     : {d}")

    d.rotate(2)              # rotate right by 2
    print(f"    Rotate right 2 : {d}")

    d.rotate(-2)             # rotate left by 2
    print(f"    Rotate left 2  : {d}")

    # ── maxlen — Fixed-size buffer (auto-drops oldest) ──
    recent = deque(maxlen=3)
    for item in ["a", "b", "c", "d", "e"]:
        recent.append(item)
        print(f"    Add '{item}': {list(recent)}")

    # ── BFS with deque ──
    print("\n    BFS (Breadth-First Search):")
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [], "E": [], "F": [],
    }

    def bfs(start):
        visited = set()
        queue = deque([start])
        order = []
        while queue:
            node = queue.popleft()  # O(1) — this is why deque is used
            if node not in visited:
                visited.add(node)
                order.append(node)
                queue.extend(graph.get(node, []))
        return order

    print(f"    BFS from 'A': {bfs('A')}")

    # ── Sliding Window with deque ──
    def sliding_window_max(nums: list, k: int) -> list:
        """Find maximum in each sliding window of size k."""
        result = []
        window = deque()  # stores indices

        for i, num in enumerate(nums):
            # Remove elements outside window
            while window and window[0] < i - k + 1:
                window.popleft()
            # Remove smaller elements (they'll never be max)
            while window and nums[window[-1]] < num:
                window.pop()
            window.append(i)
            if i >= k - 1:
                result.append(nums[window[0]])
        return result

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    print(f"\n    Sliding window max (k=3):")
    print(f"    Input  : {nums}")
    print(f"    Output : {sliding_window_max(nums, 3)}")


# ═══════════════════════════════════════════════════
# 2. DEFAULTDICT — Auto-initializing Dictionary
# ═══════════════════════════════════════════════════

def demo_defaultdict():
    # ── Grouping ──
    students = [
        ("Math", "Alice"), ("Science", "Bob"), ("Math", "Charlie"),
        ("Science", "Diana"), ("Math", "Eve"), ("Art", "Frank"),
    ]

    by_subject = defaultdict(list)
    for subject, name in students:
        by_subject[subject].append(name)

    print("    Grouped by subject:")
    for subj, names in by_subject.items():
        print(f"      {subj:10s}: {', '.join(names)}")

    # ── Counting ──
    words = "the cat sat on the mat and the cat ate the rat".split()
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
    print(f"\n    Word counts: {dict(word_count)}")

    # ── Nested defaultdict (auto-vivification) ──
    tree = lambda: defaultdict(tree)  # infinite nesting!

    config = tree()
    config["database"]["host"] = "localhost"
    config["database"]["port"] = 5432
    config["server"]["debug"] = True

    # Convert to regular dict for display
    def to_dict(d):
        if isinstance(d, defaultdict):
            return {k: to_dict(v) for k, v in d.items()}
        return d

    print(f"\n    Auto-vivification: {to_dict(config)}")

    # ── Set for unique values ──
    transactions = [
        ("Alice", "food"), ("Bob", "tech"), ("Alice", "tech"),
        ("Alice", "food"), ("Bob", "food"), ("Charlie", "tech"),
    ]
    user_categories = defaultdict(set)
    for user, cat in transactions:
        user_categories[user].add(cat)
    print(f"\n    Unique categories per user:")
    for user, cats in user_categories.items():
        print(f"      {user}: {cats}")


# ═══════════════════════════════════════════════════
# 3. COUNTER — Counting Made Easy
# ═══════════════════════════════════════════════════

def demo_counter():
    # Basic counting
    text = "abracadabra"
    c = Counter(text)
    print(f"    Counter('{text}'): {c}")

    # Most common
    print(f"    Most common 3  : {c.most_common(3)}")

    # Counter arithmetic
    c1 = Counter("aabbcc")
    c2 = Counter("abcxyz")

    print(f"\n    Counter arithmetic:")
    print(f"    c1         : {c1}")
    print(f"    c2         : {c2}")
    print(f"    c1 + c2    : {c1 + c2}")     # add counts
    print(f"    c1 - c2    : {c1 - c2}")     # subtract (drops ≤0)
    print(f"    c1 & c2    : {c1 & c2}")     # intersection (min)
    print(f"    c1 | c2    : {c1 | c2}")     # union (max)

    # Real-world: Top programming languages
    survey = [
        "Python", "JavaScript", "Python", "Java", "Python",
        "JavaScript", "C++", "Java", "Python", "Go",
        "JavaScript", "Python", "Rust", "Go", "JavaScript",
    ]
    ranking = Counter(survey).most_common()
    print(f"\n    Language ranking:")
    for i, (lang, count) in enumerate(ranking, 1):
        bar = "█" * count
        print(f"      {i}. {lang:12s} {bar} ({count})")

    # elements() — expand counter back to iterable
    c = Counter(a=3, b=2, c=1)
    print(f"\n    elements(): {list(c.elements())}")
    print(f"    total()   : {c.total()}")  # Python 3.10+


# ═══════════════════════════════════════════════════
# 4. CHAINMAP — Layered Dictionaries
# ═══════════════════════════════════════════════════

def demo_chainmap():
    """ChainMap groups dicts — lookups search each dict in order."""

    # ── Config layering pattern ──
    defaults = {"theme": "light", "lang": "en", "timeout": 30, "debug": False}
    env_vars = {"theme": "dark", "debug": True}
    cli_args = {"timeout": 10}

    # CLI args → env vars → defaults (highest priority first)
    config = ChainMap(cli_args, env_vars, defaults)

    print("    Config (CLI > ENV > defaults):")
    for key in ["theme", "lang", "timeout", "debug"]:
        print(f"      {key:10s}: {config[key]}")

    # Maps are live — changes propagate
    print(f"\n    config.maps: {config.maps}")

    # new_child creates a new layer on top
    session_overrides = config.new_child({"lang": "fr"})
    print(f"    With session override lang='fr': {session_overrides['lang']}")

    # ── Counting across scopes (like variable scoping) ──
    print(f"\n    Simulating variable scope:")
    global_scope = {"x": 1, "y": 2}
    local_scope = {"x": 10, "z": 30}
    scope = ChainMap(local_scope, global_scope)

    for var in ["x", "y", "z"]:
        print(f"      {var} = {scope[var]}")
    # x=10 (local wins), y=2 (global), z=30 (local)


# ═══════════════════════════════════════════════════
# 5. ORDEREDDICT — Ordered Operations
# ═══════════════════════════════════════════════════

def demo_ordereddict():
    """
    Since Python 3.7, regular dicts maintain insertion order.
    But OrderedDict still has unique features:
    """
    od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])

    # move_to_end — LRU cache pattern
    od.move_to_end("a")          # move to last
    print(f"    move 'a' to end  : {list(od.items())}")

    od.move_to_end("c", last=False)  # move to first
    print(f"    move 'c' to front: {list(od.items())}")

    # popitem — LIFO/FIFO
    print(f"    popitem(last=True) : {od.popitem(last=True)}")
    print(f"    Remaining          : {list(od.items())}")

    # OrderedDict compares ORDER, regular dict doesn't
    d1 = OrderedDict([("a", 1), ("b", 2)])
    d2 = OrderedDict([("b", 2), ("a", 1)])
    print(f"\n    OrderedDict order-sensitive: {d1 == d2}")  # False

    r1 = {"a": 1, "b": 2}
    r2 = {"b": 2, "a": 1}
    print(f"    Regular dict order-agnostic : {r1 == r2}")  # True


# ═══════════════════════════════════════════════════
# 6. PERFORMANCE COMPARISON
# ═══════════════════════════════════════════════════

def demo_performance():
    """deque vs list performance for front operations."""
    N = 100_000

    # List append left (insert at 0) — O(n)
    start = time.perf_counter()
    lst = []
    for i in range(N):
        lst.insert(0, i)
    list_time = time.perf_counter() - start

    # Deque append left — O(1)
    start = time.perf_counter()
    dq = deque()
    for i in range(N):
        dq.appendleft(i)
    deque_time = time.perf_counter() - start

    print(f"    Prepend {N:,} items:")
    print(f"      list.insert(0) : {list_time:.4f}s")
    print(f"      deque.appendleft: {deque_time:.4f}s")
    print(f"      Speedup        : {list_time/deque_time:.0f}x faster 🚀")


# ─────────────────────────────────────────────────
# DEMO
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    sections = [
        ("1. deque — Double-Ended Queue", demo_deque),
        ("2. defaultdict — Auto-Initializing Dict", demo_defaultdict),
        ("3. Counter — Counting & Ranking", demo_counter),
        ("4. ChainMap — Layered Lookups", demo_chainmap),
        ("5. OrderedDict — Order-Aware Dict", demo_ordereddict),
        ("6. Performance: deque vs list", demo_performance),
    ]
    for title, fn in sections:
        print("\n" + "=" * 55)
        print(title)
        print("=" * 55)
        fn()
