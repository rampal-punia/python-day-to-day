# Parameters VS Arguments in Python

In Python, the terms "argument" and "parameter" are often used interchangeably, but they have slightly different meanings.

Understanding the difference between these two terms is essential to write clean and efficient code. This tutorial will explain the difference between arguments and parameters in Python with the required codes.

## Parameters (PlaceHolder Values)

Parameters are the input variables that are defined when defining a function. They serve as placeholders for the actual values that will be passed to the function when it is called.

In Python, parameters are defined within the parentheses of a function definition.

Let's take a look at an example:

```python
def area(length, width):
    # 👉 Parameters: length, width (Placeholder Values)
    return length * width
```

In this example, length and width are the parameters of the `area()` function. When this function is called, the value that is passed to length and width will be used to generate the value for return statement.

## Arguments (Actual Values)

Arguments are the actual values that are passed to a function when it is called. In other words, they are the values that are used to replace the placeholders (parameters) in the function definition.

In Python, arguments are passed within the parentheses of a function call.

Let's see an example:

```python
def area(length, width):
    # 👉 Parameters: length, width (Placeholder Values)
    return length * width


# 👉 Arguments: 10, 20 (Actual values)
result = area(10, 20)
print(result)
```

In this example, 10, and 20 are the arguments that is passed to the `area()` function. When the function is called, 10 and 20 are used to replace the length and width parameters in the function definition. As a result, the function returns `10 * 20 = 200` to the console.

## Difference between Arguments and Parameters

The difference between arguments and parameters in Python can be summarized as follows:

- Parameters are the placeholders defined in a function definition.
- Arguments are the actual values passed to a function when it is called.
- The number of parameters in a function definition is fixed, whereas the number of arguments that can be passed to a function can vary.
- If a function is called with too few or too many arguments, a TypeError is raised.
- Parameters are used to define a function's signature, while arguments are used to invoke the function.

Let's see an example that demonstrates the difference between arguments and parameters in Python.

```python
def addition(x, y):
    return x + y

result = addition(2, 3)
print(result)
```

In this example, `addition()` function takes two parameters, x and y. When the function is called with `addition(2, 3)`, 2 and 3 are the arguments that are passed to the function. These arguments replace the x and y parameters in the function definition. As a result, the function returns 5, which is assigned to the result variable.

## How to remember

Simply reiterate this:

- Parameters (P) ==> Placeholder Values (P)
- Arguments (A) ==> Actual Values (A)

In summary, parameters are the input variables defined in a function definition, whereas arguments are the actual values passed to a function when it is called. Understanding the difference between these two terms is crucial for writing efficient and bug-free code.
