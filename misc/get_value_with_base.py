def generate_value_from_base(value, base=10):
    value = str(value)
    result = 0
    for digit in value:
        result = result * base + int(digit)
    return result


print(generate_value_from_base(20, 10))
print(generate_value_from_base(20, 2))
print(generate_value_from_base(20, 8))
print(generate_value_from_base(20, 16))
