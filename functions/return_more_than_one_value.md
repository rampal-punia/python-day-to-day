# Returning Multiple Values from a Function in Python

In Python, you can return multiple values from a function by returning them as a tuple. A tuple is a data structure defined by a list of comma-separated values without any outer brackets.

Let's start with a simple example:

```python
data = 1, 2, 3
print(type(data))
```

Output:

```bash
<class 'tuple'>
```

As you can see, if you put two comma-separated values in a return statement, it will become a tuple. You can iterate over the values in the same way as you would with a tuple.

Here's an example of returning multiple values from a function:

```python
def add_subtract(a, b):
    add = a + b
    subtract = a - b
    return add, subtract

result = add_subtract(10, 5)
print(result)
```

Output:

```bash
(15, 5)
```

In this example, the function `add_subtract` takes two parameters `a` and `b`, performs addition and subtraction, and returns the results as a tuple. The returned tuple is then assigned to the `result` variable.

You can also unpack the tuple returned by the function into separate variables:

```python
add, subtract = add_subtract(10, 5)
print("Addition:", add)
print("Subtraction:", subtract)
```

Output:

```bash
Addition: 15
Subtraction: 5
```

Another example:

```python
def divide_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

result = divide_remainder(19, 4)
print(f"Quotient: {result[0]}")
print(f"Remainder: {result[1]}")
```

Output:

```bash
Quotient: 4
Remainder: 3
```

In this example, the function `divide_remainder` takes two parameters `dividend` and `divisor`, performs integer division and returns the quotient and remainder as a tuple. The tuple can then be unpacked and assigned to separate variables as shown in the `result` variable.

Note: It's a best practice to have function names that describe a single, well-defined task. In this example, the function name is doing two tasks. So it is better to divide it into two separate functions. It's used here to demonstrate how to return multiple values from a function.
