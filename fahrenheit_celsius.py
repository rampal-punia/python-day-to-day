'''✨ Convert Fahrenheit to Celsius ✨'''


def validate_input(value):
    try:
        value = float(value)
        return value
    except ValueError:
        return None


fahrenheit = input("Fahrenheit value: ")
fahrenheit = validate_input(fahrenheit)

if fahrenheit is not None:
    celsius = (fahrenheit - 32) * 5/9
    print(f"Celsius value of {fahrenheit} fahrenheit is {celsius:.2f}.")
else:
    print("Please enter a valid number.")


# 🔥 -40 Fahrenheit is equal to -40 Celsius. Check it yourself.🔥
# 👩‍💻 See you soon, Till then Keep Improving!!!


# For more on Python follow: https://twitter.com/CodingMantras
