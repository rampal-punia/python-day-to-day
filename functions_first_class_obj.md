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

## Store a function in a data structures

A first-class object can be stored in data structures like lists and dictionaries, and a function in Python can be stored in data structures just like any other data type.

For example:

```python
def greet():
    print("Hello!")

greetings = [greet, greet, greet]

for greeting in greetings:
    greeting() # prints "Hello!" three times
```

## Define inside other functions

In Python, functions can be defined inside other functions, which are called nested functions.

Here's an example:

```python
def outer_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")

    inner_function() # Call the inner function

outer_function() # Call the outer function
```

In this example, the inner_function() is defined inside the outer_function().

When outer_function() is called, it prints a message and then calls inner_function().

inner_function() then prints its own message.

Note that the inner function is only accessible within the outer function, which means it can't be called from outside of the outer_function() scope.

If you try to call inner_function() outside of outer_function(), you'll get a NameError because the function is not defined.

These examples demonstrate that functions in Python are first-class objects, meaning that they can be treated just like any other object in the language and be assigned to variables, passed as arguments to other functions, and returned from functions.

1. Functions as parameters: In Python, functions can be passed as parameters to other functions. This is useful when you want to use a function as a callback function, or when you want to use a higher-order function that takes a function as input and returns a new function.
For example:

```python
def apply_operation(func, x, y):
    return func(x, y)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

result = apply_operation(add, 2, 3)   # returns 5
result = apply_operation(multiply, 2, 3)   # returns 6
```

In this example, we define a function apply_operation that takes a function func as input and two values x and y. The function apply_operation applies the function func to the values x and y and returns the result. We also define two other functions add and multiply that perform the respective operations. We then use the apply_operation function to apply the add and multiply functions to the values 2 and 3.

2. Functions as return values: In Python, functions can also be used as return values from other functions. This is useful when you want to return a new function that has certain properties, or when you want to create a closure that holds some state.
For example:

```python
def create_incrementor(n):
    def increment(x):
        return x + n
    return increment

add_five = create_incrementor(5)
result = add_five(3)   # returns 8
```

In this example, we define a function create_incrementor that takes a value n. The function create_incrementor returns a new function increment that takes a value x and adds n to it. We then use the create_incrementor function to create a new function add_five that adds 5 to any value that is passed to it. We then use the add_five function to add 5 to 3, which returns 8.

3. Functions as objects: In Python, functions are objects just like any other object. This means that you can add attributes to functions, pass them around as variables, and perform other operations on them that you would perform on objects.
For example:

```python
```

4. Functions can be defined inside other functions
In Python, you can define a function inside another function. This is known as a nested function. The nested function can access the variables of the outer function, but the outer function cannot access the variables of the nested function. Here's an example:

```python
def outer():
    x = 10

    def inner():
        print(x)

    inner()

outer() # Output: 10
```

In this example, we define a function outer() that defines a variable x and a nested function inner(). The nested function inner() prints the value of x. When we call the outer function, it calls the nested function inner() which prints the value of x.

Functions can be used to implement closures
A closure is a function that retains the values of the variables in its enclosing scope even after the execution of that scope has finished. In Python, closures are implemented using nested functions. Here's an example:

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add_5 = outer(5)
print(add_5(3)) # Output: 8
```

In this example, we define a function outer() that takes a parameter x and returns a nested function inner(). The inner function takes a parameter y and returns the sum of x and y. We then call the outer function with an argument of 5, which returns the inner function. We assign the returned function to the variable add_5 and call it with an argument of 3, which returns the sum of 5 and 3.

Functions can be used to implement decorators
A decorator is a function that takes another function as input and returns a new function that extends the behavior of the original function without modifying its code. Decorators are often used for logging, timing, and authentication. Here's an example:

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args {args} and kwargs {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

print(add(3, 5)) # Output: Calling function add with args (3, 5) and kwargs {} \n 8
```

---

## Small version

Python functions are termed first-class objects!!!

This means a python function can be:

- Created at runtime

- Stored in any data structure

- Assigned to a variable

- Passed as an argument

- Returned from a function as a result

### Here are 5 main reasons why Python functions are termed first-class objects

Assignable to variables: Functions can be assigned to variables just like any other value in Python. This means that functions can be passed around as arguments to other functions, returned from functions, and stored in data structures such as lists or dictionaries.

Passed as arguments: Functions can be passed as arguments to other functions. This is known as higher-order functions. This allows for the creation of more complex functions that take other functions as inputs.

Returned as values: Functions can also be returned as values from other functions. This is useful for creating functions that generate other functions.

Stored in data structures: Functions can be stored in data structures such as lists or dictionaries. This allows for the creation of more complex data structures that can hold functions as well as other types of data.

Can be defined inside other functions: Functions can be defined inside other functions. This allows for the creation of closures, which are functions that retain access to the variables in their enclosing scope even after the enclosing function has returned. Closures are useful for creating functions with persistent state or for creating functions that act as generators.
