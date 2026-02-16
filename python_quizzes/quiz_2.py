"""Quiz 2: str.partition() method.

Difficulty: 🟢 Easy
Topics: str.partition(), string splitting, tuple return

Question: What is the output of "Python is Awesome!".partition("is")?
    A: Python
    B: AttributeError
    C: is
    D: Awesome
"""


def quiz() -> None:
    """partition() returns a 3-tuple: (before, sep, after)."""
    my_string = "Python is Awesome!"
    parts = my_string.partition("is")

    print("── Quiz 2 ──")
    print(f"  '{my_string}'.partition('is')")
    print(f"  Result: {parts}")
    # Answer: None of the options (it's a tuple!)
    # partition() returns: ('Python ', 'is', ' Awesome!')
    # It returns a 3-tuple: (before, separator, after)


if __name__ == "__main__":
    quiz()

# For more on Python follow: https://x.com/rs_punia_
