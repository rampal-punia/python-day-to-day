"""Fahrenheit ↔ Celsius Converter — Simple temperature conversion.

Difficulty: 🟢 Easy
Topics: input validation, arithmetic, f-strings, type hints

Author: @rampal-punia
"""


def validate_input(value: str) -> float | None:
    """Validate and convert user input to a float.

    Args:
        value: The raw string input from the user.

    Returns:
        The float value if valid, or None if conversion fails.
    """
    try:
        return float(value)
    except ValueError:
        return None


def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius.

    Formula: C = (F - 32) × 5/9

    Args:
        f: Temperature in Fahrenheit.

    Returns:
        Temperature in Celsius.
    """
    return (f - 32) * 5 / 9


def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit.

    Formula: F = C × 9/5 + 32

    Args:
        c: Temperature in Celsius.

    Returns:
        Temperature in Fahrenheit.
    """
    return c * 9 / 5 + 32


if __name__ == "__main__":
    fahrenheit = input("Enter Fahrenheit value: ")
    fahrenheit = validate_input(fahrenheit)

    if fahrenheit is not None:
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"Celsius value of {fahrenheit}°F is {celsius:.2f}°C.")

        # Round-trip check: convert back to Fahrenheit
        back_to_f = celsius_to_fahrenheit(celsius)
        print(f"Verification: {celsius:.2f}°C → {back_to_f:.2f}°F")
    else:
        print("Please enter a valid number.")

    # 🔥 Fun fact: −40°F is equal to −40°C. Check it yourself!
    print(f"\n🔥 Fun fact: −40°F = {fahrenheit_to_celsius(-40):.0f}°C")


# For more on Python follow: https://x.com/rs_punia_
