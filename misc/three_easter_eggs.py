"""Python Easter Eggs — 3 hidden surprises in the interpreter.

Difficulty: 🟢 Easy
Topics: import this, __hello__, antigravity, easter eggs

1. `import this`       → The Zen of Python (19 guiding principles)
2. `import __hello__`  → "Hello world!" (Python's simplest module)
3. `import antigravity` → Opens xkcd #353 comic in your browser

Note: `import antigravity` requires an active internet connection
      and will open a browser window.

Author: @rampal-punia
"""


def show_easter_eggs() -> None:
    """Demonstrate Python's built-in easter eggs (safely)."""
    # Easter Egg 1: The Zen of Python
    print("── Easter Egg 1: The Zen of Python ──")
    print("  Run: import this")
    import this  # noqa: F401 — prints the Zen automatically

    # Easter Egg 2: Hello World
    print("\n── Easter Egg 2: Hello World ──")
    print("  Run: import __hello__")
    import __hello__  # noqa: F401 — prints "Hello world!"

    # Easter Egg 3: xkcd comic (commented out to avoid opening browser)
    print("\n── Easter Egg 3: xkcd Antigravity ──")
    print("  Run: import antigravity")
    print("  (Opens xkcd.com/353 in your browser — try it in a REPL!)")
    # import antigravity  # Uncomment to open the comic


if __name__ == "__main__":
    show_easter_eggs()

# For more on Python follow: https://x.com/rs_punia_
