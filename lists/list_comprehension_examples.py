"""List Comprehension Examples — 10 practical patterns.

Difficulty: 🟢 Easy → 🟡 Intermediate
Topics: list comprehension, dict comprehension, filtering, nested loops

Syntax: [expression for item in iterable if condition]

Author: @rampal-punia
"""

from typing import Any


def demo_list_comprehensions() -> None:
    """Demonstrate 10 common list comprehension patterns."""

    # 1. Squaring numbers
    numbers = [1, 2, 3, 4, 5]
    squares = [n**2 for n in numbers]
    print(f"  1. Squares:      {squares}")  # [1, 4, 9, 16, 25]

    # 2. Filtering even numbers
    even_numbers = [n for n in numbers if n % 2 == 0]
    print(f"  2. Evens:        {even_numbers}")  # [2, 4]

    # 3. Dict from two lists (dict comprehension)
    keys = ["a", "b", "c"]
    values = [1, 2, 3]
    dictionary = {k: v for k, v in zip(keys, values)}
    print(f"  3. Zip to dict:  {dictionary}")  # {'a': 1, 'b': 2, 'c': 3}

    # 4. Flatten a 2D list
    matrix = [[1, 2], [3, 4], [5, 6]]
    flat = [item for row in matrix for item in row]
    print(f"  4. Flatten:      {flat}")  # [1, 2, 3, 4, 5, 6]

    # 5. String to int conversion
    str_list = ["1", "2", "3", "4", "5"]
    int_list = [int(num) for num in str_list]
    print(f"  5. Str→Int:      {int_list}")  # [1, 2, 3, 4, 5]

    # 6. Common elements (intersection)
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    common = [n for n in list1 if n in list2]
    print(f"  6. Common:       {common}")  # [3, 4, 5]

    # 7. Remove duplicates (preserving order)
    dupes = [1, 2, 2, 3, 4, 4, 5]
    seen: set[int] = set()
    unique = [seen.add(n) or n for n in dupes if n not in seen]  # type: ignore
    print(f"  7. Unique:       {unique}")  # [1, 2, 3, 4, 5]

    # 8. Transpose a matrix
    matrix = [[1, 2], [3, 4], [5, 6]]
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print(f"  8. Transpose:    {transposed}")  # [[1, 3, 5], [2, 4, 6]]

    # 9. Filter only numeric values from mixed list
    mixed: list[Any] = [1, "a", 2, "b", 3.5, "c"]
    nums_only = [n for n in mixed if isinstance(n, (int, float))]
    print(f"  9. Numeric only: {nums_only}")  # [1, 2, 3.5]

    # 10. Sort list of dicts by key
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 20},
        {"name": "Charlie", "age": 30},
    ]
    sorted_people = sorted(people, key=lambda x: x["age"])
    names_by_age = [p["name"] for p in sorted_people]
    print(f"  10. Sorted:      {names_by_age}")  # ['Bob', 'Alice', 'Charlie']


if __name__ == "__main__":
    print("── List Comprehension Patterns ──")
    demo_list_comprehensions()

# For more on Python follow: https://x.com/rs_punia_
