'''✨ Python: Convert A Given Temperature Value. ✨
Points:
    - Convert Celsius to Fahrenheit an Vice-Versa.
    - Validate input for strings or any text-mix values.
    - Validate Input for absolute zero(Temperature above absolute zero only).
'''


class Temperature:
    def __init__(self, value=0, unit='C'):
        self.value, self.unit = self._validate_input(value, unit)

    def _validate_input(self, value, unit):
        try:
            value = float(value)
            if unit == 'C' and value < -273.15:
                raise ValueError(
                    "Temperature can't go below absolute zero in Celsius")
            elif unit == 'F' and value < -459.67:
                raise ValueError(
                    "Temperature can't go below absolute zero in Fahrenheit")
            return value, unit
        except ValueError:
            return None, None

    def to_celsius(self):
        if self.unit == 'F':
            self.value = (self.value - 32) * 5/9
            self.unit = 'C'
        return self.value

    def to_fahrenheit(self):
        if self.unit == 'C':
            self.value = (self.value * 9/5) + 32
            self.unit = 'F'
        return self.value


value = input("Enter temperature value: ")
unit = input("Enter temperature unit (C or F): ")
temp = Temperature(value, unit)

if temp.value is not None:
    print(f"Temperature in Celsius: {temp.to_celsius():.2f}")
    print(f"Temperature in Fahrenheit: {temp.to_fahrenheit():.2f}")
else:
    print("Please enter a valid temperature value and unit.")


# 🔥 -40 Fahrenheit is equal to -40 Celsius. Check it yourself.🔥
# 👩‍💻 See you soon, Till then Keep Improving!!!


# For more on Python follow: https://twitter.com/CodingMantras
