"""Quiz 18: yield keyword — generator function.

Difficulty: 🟡 Intermediate
Topics: yield, generator, range, lazy evaluation

Question: What is the output?
    A) 1 4 9 16 25
    B) 1 4 9 16
    C) 1 4 9 16 25 36 49 64 81
    D) Error, as no return statement inside function
"""

from collections.abc import Generator


def square(start: int = 1, stop: int = 10) -> Generator[int, None, None]:
    """Yield squares of numbers in range [start, stop)."""
    for n in range(start, stop):
        yield n * n


def quiz() -> None:
    """yield makes square() a generator, not a regular function."""
    print("── Quiz 18 ──  ", end="")
    for i in square(start=1, stop=5):
        print(i, end=" ")
    print()

    # Answer: B) 1 4 9 16
    # range(1, 5) = [1, 2, 3, 4]  (stop=5 is exclusive)
    # Squares: 1²=1, 2²=4, 3²=9, 4²=16
    # yield does NOT require a return statement.
    # Functions with yield become generators.


if __name__ == "__main__":
    quiz()

# For more on Python follow: https://x.com/rs_punia_
