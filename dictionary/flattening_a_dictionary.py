"""Flattening Dictionaries — From one level to deeply nested.

Difficulty: 🟢 Easy → 🟡 Intermediate
Topics: dict comprehension, itertools.chain, recursion, separator keys

Author: @rampal-punia
"""

import itertools
from typing import Any


# ── 🟢 Method 1: Dict comprehension (one level deep) ──


def flatten_one_level(nested: dict[Any, dict]) -> dict:
    """Flatten a dict whose values are all dicts (one level only).

    Args:
        nested: Dict like {1: {2: 3}, 4: {5: 6}}.

    Returns:
        Flattened dict like {2: 3, 5: 6}.
    """
    return {k: v for d in nested.values() if isinstance(d, dict) for k, v in d.items()}


# ── 🟢 Method 2: itertools.chain (one level deep) ──


def flatten_with_chain(nested: dict[Any, dict]) -> dict:
    """Flatten using itertools.chain.from_iterable."""
    return dict(
        itertools.chain.from_iterable(
            d.items() for d in nested.values() if isinstance(d, dict)
        )
    )


# ── 🟡 Method 3: Recursive flatten with separator keys (any depth) ──


def flatten_deep(nested: dict, parent_key: str = "", sep: str = ".") -> dict[str, Any]:
    """Recursively flatten a deeply nested dictionary.

    Nested keys are joined with a separator.
    {'a': {'b': {'c': 1}}} → {'a.b.c': 1}

    Args:
        nested: The dictionary to flatten.
        parent_key: Prefix for current level (used in recursion).
        sep: Separator between nested keys (default: '.').

    Returns:
        A flat dictionary with composite keys.
    """
    items: list[tuple[str, Any]] = []
    for key, value in nested.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)
        if isinstance(value, dict):
            items.extend(flatten_deep(value, new_key, sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


if __name__ == "__main__":
    # ── One-level flattening ──
    print("── One-Level Flattening ──")
    simple = {1: {2: 3}, 4: {5: 6}}
    print(f"  Input:  {simple}")
    print(f"  Method 1 (comprehension): {flatten_one_level(simple)}")
    print(f"  Method 2 (chain):         {flatten_with_chain(simple)}")

    # ── Deep flattening ──
    print("\n── Deep Flattening (recursive) ──")
    deep = {
        "user": {
            "name": "Alice",
            "address": {
                "city": "Wonderland",
                "coordinates": {"lat": 51.5, "lng": -0.1},
            },
            "age": 30,
        },
        "active": True,
    }
    print(f"  Input:    {deep}")
    flat = flatten_deep(deep)
    for key, value in flat.items():
        print(f"  '{key}' → {value}")

# For more on Python follow: https://x.com/rs_punia_
