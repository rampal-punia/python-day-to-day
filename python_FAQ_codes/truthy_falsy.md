# A Quick Overview: Truthy and Falsy Values in Python

In Python, certain data types are considered "truthy" and others are considered "falsy."

These terms refer to whether or not a value is evaluated as True or False in a boolean context.

## Falsy values

- None

- False

- Zero of any numeric type (e.g. 0, 0.0, 0j)

- Empty sequences (e.g. '', (), [])

- Empty containers (e.g. {}, set())

- Instances of user-defined classes that define a bool() or len() method that returns False or 0 respectively.

## Truthy values

All other non-falsy values, such as:

- numbers other than 0
- strings that are not empty
- lists or tuples that are not empty

- Instances of user-defined classes that define a bool() or len() method that returns True or any non-zero value respectively.

## Check for Truthy and Falsy Values

In Python, we use the built-in bool() function to check if an object is truthy or falsy.

### bool() function

The bool() function returns True for truthy values and False for falsy values.

For example:

```python
value = 0
result = bool(value)
print(result) # False (0 is falsy)

value = "Hello"
result = bool(value)
print(result) # True ("Hello" is truthy)
```

### not operator

We can also use the not operator as well:

```python
value = 0
result = not value
print(result) # True (0 is falsy)

value = "Hello"
result = not value
print(result) # False ("Hello" is truthy)
```

In summary, you can use the bool() function or the not operator to check if an object in Python is truthy or falsy.
