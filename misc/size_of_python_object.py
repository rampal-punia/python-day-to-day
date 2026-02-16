"""Size of Python Objects — Compare memory usage with sys.getsizeof.

Difficulty: 🟢 Easy
Topics: sys.getsizeof, memory, tuple vs list vs dict vs namedtuple

Key insight:
    tuple       ≈ 64 bytes  (immutable, compact)
    namedtuple  ≈ 64 bytes  (same as tuple, with named access)
    list        ≈ 88 bytes  (mutable, needs extra overhead)
    dict        ≈ 232 bytes (hash table overhead)

Note: getsizeof() returns SHALLOW size only — it doesn't follow
references to the actual string objects stored inside.

Author: @rampal-punia
"""

import sys
from collections import namedtuple


def compare_container_sizes() -> None:
    """Compare memory usage of different container types."""
    data = ("Python", "Ruby", "C++")

    # Tuple
    languages_tuple = data

    # List
    languages_list = list(data)

    # Dict
    languages_dict = {"a": data[0], "b": data[1], "c": data[2]}

    # NamedTuple
    Languages = namedtuple("Languages", ["a", "b", "c"])
    languages_nt = Languages(**languages_dict)

    containers = [
        ("tuple", languages_tuple),
        ("namedtuple", languages_nt),
        ("list", languages_list),
        ("dict", languages_dict),
    ]

    print("── Container Memory Comparison ──")
    print(f"  {'Type':<14} {'Size (bytes)':>12}  Value")
    print(f"  {'-'*14} {'-'*12}  {'-'*30}")
    for name, obj in containers:
        size = sys.getsizeof(obj)
        print(f"  {name:<14} {size:>12}  {obj}")

    # Also compare scalars
    print("\n── Scalar Memory Sizes ──")
    scalars = [0, 1, 256, 3.14, True, None, "", "hello", b"hello"]
    for val in scalars:
        print(f"  {type(val).__name__:<8} {repr(val):<12} = {sys.getsizeof(val)} bytes")


if __name__ == "__main__":
    compare_container_sizes()
