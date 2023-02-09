# Functions as First Class Object

In Python, a function is a first-class object, which means that it can be treated just like any other object (e.g. int, str, list, etc.).

In other words, a function can be assigned to a variable, passed as an argument to another function, returned from a function and stored in any data structures just like any other object.

## Assigning a function to a variable

Here's an example of assigning a function to a variable:

```python
def greet(name):
    print("Hello, " + name + "!")

greet_func = greet

greet_func("John")  # Output: Hello, John!
```

In the above example, we define a function `greet(name)` that takes a single argument name and prints a greeting message. We then assign the function to the variable `greet_func`. We can then call the function by invoking the variable name `greet_func`("John") and it will execute the function `greet()`.

## Passing a function as an argument to another function

Here's an example of passing a function as an argument to another function:

```python
def execute_func(func, arg):
    func(arg)

execute_func(greet, "Mary")  # Output: Hello, Mary!
```

In this example, we define a function execute_func(func, arg) that takes two arguments: a function func and an argument arg. The function then calls the passed function func(arg). We pass the greet function as the first argument and "Mary" as the second argument to the execute_func() which will call the greet function with "Mary" as the argument.

## Returning a function from a function

Here's an example of returning a function from a function:

```python
def create_greeting_func(name):
    def greet():
        print("Hello, " + name + "!")
    return greet

new_greet_func = create_greeting_func("John")
new_greet_func()  # Output: Hello, John!
```

In this example, we define a function `create_greeting_func(name)` that takes a single argument `name`. The function defines and returns another function `greet()` that prints a greeting message using the passed argument name. We then assign the returned function to the variable `new_greet_func` and call it, which will execute the inner function `greet()`

## Stored a function in a data structures

A first-class object can be stored in data structures like lists and dictionaries, and a function in Python can be stored in data structures just like any other data type.

For example:

```python
def greet():
    print("Hello!")

greetings = [greet, greet, greet]

for greeting in greetings:
    greeting() # prints "Hello!" three times
```

These examples demonstrate that functions in Python are first-class objects, meaning that they can be treated just like any other object in the language and be assigned to variables, passed as arguments to other functions, and returned from functions.
