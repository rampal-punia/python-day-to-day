"""Sort a List of Tuples — 5 methods to sort by the second element.

Difficulty: 🟢 Easy → 🟡 Intermediate
Topics: sorted(), list.sort(), lambda, key function, operator.itemgetter

All methods sort by the SECOND element (index 1) of each tuple.

Author: @rampal-punia
"""

from operator import itemgetter


def demo_sorting_methods() -> None:
    """Demonstrate 5 ways to sort a list of tuples by second element."""
    data = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

    # Method 1: sorted() with lambda (returns new list)
    result1 = sorted(data, key=lambda x: x[1])
    print(f"  1. sorted + lambda:     {result1}")

    # Method 2: list.sort() with lambda (in-place)
    data2 = data.copy()
    data2.sort(key=lambda x: x[1])
    print(f"  2. sort in-place:       {data2}")

    # Method 3: Named key function (more readable)
    def by_second(t: tuple[int, int]) -> int:
        return t[1]

    result3 = sorted(data, key=by_second)
    print(f"  3. Named key function:  {result3}")

    # Method 4: operator.itemgetter (fastest for simple cases)
    result4 = sorted(data, key=itemgetter(1))
    print(f"  4. itemgetter(1):       {result4}")

    # Method 5: Insertion sort (educational / manual)
    data5 = data.copy()
    for i in range(1, len(data5)):
        j = i
        while j > 0 and data5[j - 1][1] > data5[j][1]:
            data5[j], data5[j - 1] = data5[j - 1], data5[j]
            j -= 1
    print(f"  5. Insertion sort:      {data5}")

    # Verify all match
    assert result1 == data2 == result3 == result4 == data5
    print("\n  All 5 methods produce the same result.")


if __name__ == "__main__":
    print("── Sorting Tuples by Second Element ──\n")
    demo_sorting_methods()
