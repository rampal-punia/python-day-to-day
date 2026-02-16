"""Quiz 7: list.append() returns None.

Difficulty: 🟢 Easy
Topics: list.append(), return value, in-place mutation

Question: What is the output?
    A) [1, 2, 3, 4]
    B) [1, 2, 3, 4, 4]
    C) None
    D) [4]
"""


def quiz() -> None:
    """append() mutates in place and returns None."""
    my_list = list(range(1, 4))  # [1, 2, 3]
    my_list.append(4)

    print("── Quiz 7 ──")
    print(f"  my_list after append(4): {my_list}")
    # Answer: A) [1, 2, 3, 4]

    # But be careful with this pattern:
    result = my_list.append(5)  # Returns None!
    print(f"  result = my_list.append(5): {result}")
    print(f"  my_list is now: {my_list}")
    # append() modifies the list IN PLACE and returns None.


if __name__ == "__main__":
    quiz()

# For more on Python follow: https://x.com/rs_punia_
