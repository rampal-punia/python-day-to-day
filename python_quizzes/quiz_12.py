"""Quiz 12: set.difference() — returns a NEW set.

Difficulty: 🟡 Intermediate
Topics: set.difference(), difference vs difference_update

Question: What is set1 after calling set1.difference(set2)?
    A) {1, 2, 3, 4, 5, 6, 7}
    B) {1, 2}
    C) {1, 2, 3, 4, 5}  (unchanged!)
    D) {6, 7}
"""


def quiz() -> None:
    """difference() returns a NEW set; the original is unchanged."""
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    result = set1.difference(set2)

    print("── Quiz 12 ──")
    print(f"  result = set1.difference(set2)")
    print(f"  result = {result}")  # {1, 2}
    print(f"  set1   = {set1}")  # {1, 2, 3, 4, 5} — UNCHANGED!

    # Answer: C) {1, 2, 3, 4, 5} (set1 is unchanged)
    # Key difference from quiz 11:
    #   .difference()        → returns NEW set, original unchanged
    #   .difference_update() → modifies set IN PLACE, returns None
    print("\n  .difference()        → new set, original unchanged")
    print("  .difference_update() → modifies in place, returns None")


if __name__ == "__main__":
    quiz()

# For more on Python follow: https://x.com/rs_punia_
