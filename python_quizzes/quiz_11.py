"""Quiz 11: set.difference_update() — modifies in place.

Difficulty: 🟡 Intermediate
Topics: set.difference_update(), in-place mutation

Question: What is set1 after set1.difference_update(set2)?
    A) {1, 2, 3, 4, 5, 6, 7}
    B) {1, 2}
    C) {3, 4, 5}
    D) {6, 7}
"""


def quiz() -> None:
    """difference_update() removes common elements IN PLACE."""
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    set1.difference_update(set2)

    print("── Quiz 11 ──")
    print(f"  set1.difference_update(set2)")
    print(f"  set1 = {set1}")
    # Answer: B) {1, 2}
    # difference_update() removes all elements found in set2
    # from set1, modifying set1 in place. Returns None.


if __name__ == "__main__":
    quiz()

# For more on Python follow: https://x.com/rs_punia_
