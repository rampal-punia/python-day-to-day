"""Quiz 3: Trailing comma creates a tuple.

Difficulty: 🟢 Easy
Topics: tuple packing, trailing comma, type()

Question: What is the output of type(t) when t = 1, ?
    A: <class 'int'>
    B: <class 'tuple'>
    C: Error
"""


def quiz() -> None:
    """A trailing comma creates a single-element tuple."""
    t = (1,)

    print("── Quiz 3 ──")
    print(f"  t = 1,")
    print(f"  type(t) = {type(t)}")
    # Answer: B  <class 'tuple'>
    # The comma after 1 makes it a tuple, not the parentheses.


if __name__ == "__main__":
    quiz()

# For more on Python follow: https://x.com/rs_punia_
