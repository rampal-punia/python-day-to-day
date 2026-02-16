"""Quiz 8: Unpacking with * (splat operator).

Difficulty: 🟡 Intermediate
Topics: unpacking, splat operator, list(), starred expression

Question: Which method works?
    A) Only Method A will work
    B) Only Method B will work
    C) Both methods (A & B) will work
    D) Both methods will generate an Error
"""


def quiz() -> None:
    """[*original] works, but list(*original) does NOT."""
    print("── Quiz 8 ──")

    # Method A: Unpacking into a new list literal
    original_list = [1, 2, 3]
    new_list_a = [*original_list]
    print(f"  Method A: [*original]    = {new_list_a}")  # Works!

    # Method B: list(*original) passes 3 separate args to list()
    original_list = [1, 2, 3]
    try:
        new_list_b = list(*original_list)  # type: ignore
        print(f"  Method B: list(*original) = {new_list_b}")
    except TypeError as e:
        print(f"  Method B: list(*original) = TypeError: {e}")

    # Answer: A) Only Method A will work
    # Explanation:
    #   [*original] unpacks into a list literal → [1, 2, 3]
    #   list(*original) unpacks to list(1, 2, 3) which is
    #   3 separate arguments → TypeError
    print("\n  [*lst] unpacks INTO a list literal")
    print("  list(*lst) unpacks AS function arguments")


if __name__ == "__main__":
    quiz()

# For more on Python follow: https://x.com/rs_punia_
