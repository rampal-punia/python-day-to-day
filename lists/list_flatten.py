"""Flatten Nested Lists — Multiple methods from basic to recursive.

Difficulty: 🟢 Easy → 🟡 Intermediate
Topics: nested lists, list comprehension, itertools.chain, recursion

Author: @rampal-punia
"""

import itertools
from typing import Any


# 🟢 Method 1: List comprehension (one level)
def flatten_comprehension(nested: list[list]) -> list:
    """Flatten a 2D list using list comprehension."""
    return [item for sublist in nested for item in sublist]


# 🟢 Method 2: itertools.chain
def flatten_chain(nested: list[list]) -> list:
    """Flatten using itertools.chain.from_iterable."""
    return list(itertools.chain.from_iterable(nested))


# 🟡 Method 3: Recursive (any depth)
def flatten_deep(nested: list[Any]) -> list[Any]:
    """Recursively flatten a list of any nesting depth.

    Args:
        nested: A list that may contain sublists at any depth.

    Returns:
        A flat list of all leaf elements.
    """
    result: list[Any] = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_deep(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    # One-level nested
    simple = [[1, 2], [3, 4], [5, 6]]
    print("── One-Level Flattening ──")
    print(f"  Input:         {simple}")
    print(f"  Comprehension: {flatten_comprehension(simple)}")
    print(f"  Chain:         {flatten_chain(simple)}")

    # Deep nested
    deep = [1, [2, [3, [4, [5]]]], 6, [[7, 8], 9]]
    print("\n── Deep Flattening (recursive) ──")
    print(f"  Input:  {deep}")
    print(f"  Output: {flatten_deep(deep)}")

# For more on Python follow: https://x.com/rs_punia_
