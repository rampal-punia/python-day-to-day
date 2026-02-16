"""Single vs Double Quotes — When to use which in Python strings.

Difficulty: 🟢 Easy
Topics: string literals, f-strings, escape characters, quoting rules

Python treats 'single' and "double" quotes identically. The choice
is purely about readability and avoiding escape characters.

Author: @rampal-punia
"""


def quoting_basics() -> None:
    """Demonstrate single and double quote usage."""
    print("── Basic Quoting Rules ──")

    # Both are equivalent
    s1 = "Hello"
    s2 = "Hello"
    print(f"  'Hello' == \"Hello\" → {s1 == s2}")  # True

    # Use double quotes when string contains an apostrophe
    sentence = "What's your name?"
    print(f"  {sentence}")

    # Use single quotes when string contains double quotes
    quote = 'He said, "Python is great!"'
    print(f"  {quote}")

    # Use escape characters when you need both
    mixed = 'He said, "What\'s your name?"'
    print(f"  {mixed}")


def fstring_quoting() -> None:
    """Demonstrate f-string quoting (Python 3.12+ allows nested quotes)."""
    print("\n── f-string Quoting ──")

    user_data = {"name": "Mark", "country": "Canada", "age": 22}

    # ✅ Different quote types inside f-string
    print(f"  Name: {user_data['name']}")
    print(f'  Country: {user_data["country"]}')

    # ✅ Using expressions inside f-strings
    print(f"  Greeting: {'Hello, ' + user_data['name']}")


def triple_quotes() -> None:
    """Show triple-quoted strings for multi-line content."""
    print("\n── Triple Quotes (multi-line) ──")

    poem = """Roses are red,
    Violets are blue,
    Python is great,
    And so are you!"""
    print(f"  {poem}")

    # Triple quotes can contain both ' and " without escaping
    dialog = """She said, "It's a beautiful day!" """
    print(f"  {dialog}")


def raw_strings() -> None:
    """Show raw strings (r'...') — backslashes are literal."""
    print("\n── Raw Strings ──")

    # Normal string: \n becomes a newline
    normal = "Line1\nLine2"
    print(f"  Normal:  {normal!r} → has newline")

    # Raw string: \n stays as literal \n
    raw = r"Line1\nLine2"
    print(f"  Raw:     {raw!r} → literal backslash-n")

    # Useful for regex and Windows paths
    path = r"C:\Users\ram\Documents"
    print(f"  Windows path: {path}")


if __name__ == "__main__":
    quoting_basics()
    fstring_quoting()
    triple_quotes()
    raw_strings()

# For more on Python follow: https://x.com/rs_punia_
