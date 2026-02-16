"""Temperature Class — OOP approach to temperature conversion.

Difficulty: 🟡 Intermediate
Topics: classes, operator overloading, validation, property, __repr__

This builds on fahrenheit_celsius_simple.py by introducing:
- Class-based design with encapsulation
- Operator overloading (__sub__, __repr__, __str__)
- Input validation with meaningful errors
- Immutable conversions (return new Temperature, don't mutate self)

Author: @rampal-punia
"""


class Temperature:
    """Represents a temperature value with unit (Celsius or Fahrenheit).

    Supports conversion between units and subtraction of temperatures.
    Conversions return new Temperature objects — the original is never mutated.

    Attributes:
        value: The numeric temperature value.
        unit: The temperature unit, either 'C' or 'F'.
    """

    ABSOLUTE_ZERO_C = -273.15
    ABSOLUTE_ZERO_F = -459.67

    def __init__(self, value: float | int = 0, unit: str = "C") -> None:
        self.value, self.unit = self._validate(value, unit)

    def _validate(self, value: float | int | str, unit: str) -> tuple[float, str]:
        """Validate and normalize temperature value and unit.

        Args:
            value: Temperature value (will be converted to float).
            unit: Must be 'C' or 'F'.

        Returns:
            Tuple of (validated_value, validated_unit).

        Raises:
            ValueError: If value can't be converted or is below absolute zero.
            TypeError: If unit is not 'C' or 'F'.
        """
        try:
            value = float(value)
        except (ValueError, TypeError):
            raise ValueError(f"Cannot convert {value!r} to a numeric temperature")

        unit = unit.upper()
        if unit not in ("C", "F"):
            raise TypeError(f"Unit must be 'C' or 'F', got {unit!r}")

        if unit == "C" and value < self.ABSOLUTE_ZERO_C:
            raise ValueError(
                f"{value}°C is below absolute zero ({self.ABSOLUTE_ZERO_C}°C)"
            )
        if unit == "F" and value < self.ABSOLUTE_ZERO_F:
            raise ValueError(
                f"{value}°F is below absolute zero ({self.ABSOLUTE_ZERO_F}°F)"
            )
        return value, unit

    def to_celsius(self) -> "Temperature":
        """Return a new Temperature in Celsius (does NOT mutate self).

        Returns:
            A new Temperature object in Celsius.
        """
        if self.unit == "C":
            return Temperature(self.value, "C")
        celsius_val = (self.value - 32) * 5 / 9
        return Temperature(celsius_val, "C")

    def to_fahrenheit(self) -> "Temperature":
        """Return a new Temperature in Fahrenheit (does NOT mutate self).

        Returns:
            A new Temperature object in Fahrenheit.
        """
        if self.unit == "F":
            return Temperature(self.value, "F")
        fahrenheit_val = self.value * 9 / 5 + 32
        return Temperature(fahrenheit_val, "F")

    def __sub__(self, other: "Temperature") -> "Temperature":
        """Subtract two temperatures (result always in Celsius).

        Args:
            other: Another Temperature object to subtract.

        Returns:
            A new Temperature representing the difference in °C.

        Raises:
            TypeError: If other is not a Temperature instance.
        """
        if not isinstance(other, Temperature):
            raise TypeError(f"Cannot subtract {type(other).__name__} from Temperature")
        # Convert both to Celsius for subtraction, without mutating either
        self_c = self.to_celsius().value
        other_c = other.to_celsius().value
        return Temperature(self_c - other_c, "C")

    def __repr__(self) -> str:
        return f"Temperature({self.value}, '{self.unit}')"

    def __str__(self) -> str:
        return f"{self.value:.2f}°{self.unit}"


if __name__ == "__main__":
    # ── Demo with hardcoded values (no user input needed) ──
    print("── Temperature Conversion Demo ──\n")

    t1 = Temperature(100, "C")
    print(f"  {t1} → {t1.to_fahrenheit()}")  # 100°C → 212°F

    t2 = Temperature(32, "F")
    print(f"  {t2} → {t2.to_celsius()}")  # 32°F → 0°C

    diff = t1 - t2
    print(f"  Difference: {t1} - {t2} = {diff}")

    # Verify -40 is the same in both scales
    t3 = Temperature(-40, "C")
    print(f"\n  🔥 Fun fact: {t3} = {t3.to_fahrenheit()}")

    # Error handling demo
    print("\n── Error Handling ──")
    for bad_input in [("abc", "C"), (-500, "C"), (100, "X")]:
        try:
            Temperature(*bad_input)
        except (ValueError, TypeError) as e:
            print(f"  Temperature{bad_input} → {e}")


# For more on Python follow: https://x.com/rs_punia_
