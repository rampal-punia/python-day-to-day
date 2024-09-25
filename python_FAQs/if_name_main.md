# What does if __name__ == '__main__' mean?

In Python, `if __name__ == '__main__'` is a common construct that is often used to make a module both importable and executable. In this tutorial, we will explore what this construct does, how it works, and how to use it in your Python code.

The `if __name__ == '__main__'` construct is a conditional statement that checks whether the current script is being run as the main program or if it is being imported as a module by another script.

When a Python file is run directly as the main program, the value of the special variable `__name__` is set to `__main__`. However, when a Python file is imported as a module by another script, the value of `__name__` is set to the name of the module.

By using the `if __name__ == '__main__'` construct, you can specify code that should only be executed when the file is run as the main program, and not when it is imported as a module.

So, the first question arises:

## What is the difference between a Python Script and A Python module?

A Python module is a file containing Python definitions and statements. It is used to organize code into logical, reusable chunks. A module can define functions, classes, and variables, and can also include runnable code. Modules are meant to be imported and used in other programs.

For example, the math module in Python provides various mathematical functions like sqrt, cos, sin, etc.

On the other hand, a Python script is a file containing a sequence of Python statements that are executed when the file is run. Scripts are used to automate tasks, run standalone programs, or test functionality. Scripts are typically standalone programs, unlike modules, which are meant to be imported and used in other programs.

Here is an example of a Python module:

```python
# file: math_ops.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

This module contains four functions that perform basic mathematical operations. The functions can be imported and used in other programs. Here's an example of how to use this module in another Python program:

```python
# file: main.py

import math_ops

a = 5
b = 3

print(math_ops.add(a, b))
print(math_ops.subtract(a, b))
print(math_ops.multiply(a, b))
print(math_ops.divide(a, b))
```

This program imports the `math_ops` module and uses its functions to perform various mathematical operations on two numbers.

Now let's look at an example of a Python script:

```python
# file: hello.py

name = input("What is your name? ")

print("Hello, " + name + "!")
```

This script prompts the user for their name and then prints a personalized greeting. To run this script, you can use the following command in your terminal or command prompt:

```bash
python hello.py
```

This will execute the script and prompt the user for their name. Once the name is entered, the script will print out the greeting.

In summary, while both Python modules and Python scripts are text files containing Python code, they have different purposes and use cases. Modules are meant to be imported and used in other programs, while scripts are standalone programs that can be executed on their own from the command line or terminal.

Now we can move further and understand how `if __name__ == '__main__'` construct help us to make a python file both a module as well as a script.

## How to use if __name__ == '__main__'

The most common use of `if __name__ == '__main__'` is to define a block of code that should only be executed when the Python file is run as the main program. Here's an example:

```python
# example.py

def main():
    print('Hello, world!')

if __name__ == '__main__':
    main()
```

In this example, the `main()` function is defined to print a message to the console. The `if __name__ == '__main__'` statement checks whether the current script is being run as the main program, and if it is, it calls the `main()` function to execute the code.

When you run this script from the command line using python `example.py`, the main() function will be executed and the message "Hello, world!" will be printed to the console.

However, if you import this script as a module in another Python file, the `main()` function will not be executed, since the `if __name__ == '__main__'` statement will evaluate to False.

So in Python, `__name__`is a special variable that contains the name of the current module. When a Python script is executed, the interpreter sets the `__name__` variable of the script to `"__main__"`. This means that if you have a Python script that you want to use both as a standalone program and as a module that can be imported by other scripts, you can use the `__name__` variable to determine if the script is being run as a standalone program or as a module

Here's an example of how to import this script as a module:

```python
import example

# Nothing is printed when importing the module
```

Here's another example that demonstrates how the `__name__` variable works:

```python
# example2.py

def say_hello(name):
    print(f"Hello, {name}!")

print(f"__name__ is {__name__}")

if __name__ == "__main__":
    say_hello("Alice")
```

Now, if you run this script from the command line with `python example2.py`, you will see the following output:

```python
__name__ is __main__
Hello, Alice!
```

The output shows that the `__name__` variable is set to `"__main__"`, and that the `say_hello()` function is called with the argument `"Alice"`. However, if you import the example2 module into another script with `import example2`, you will see the following output:

```python
__name__ is example2
```

The output shows that the `__name__` variable is set to "example2", and that the `say_hello()` function is not called, since it is inside the `if __name__ == "__main__":` block.

### Benefits of using if __name__ == '__main__'

Using the `if __name__ == '__main__'` construct has several benefits:

- It allows you to separate code that should only be run when the script is run as the main program from code that can be reused as a module in other programs.

- It makes your code more modular and easier to test, since you can import individual functions and classes from the script without executing the main program.

### Conclusion

In summary, the `if __name__ == "__main__":` statement is a useful way to ensure that code is only executed when a Python script is run as a standalone program, and not when it is imported as a module. By checking the value of the `__name__` variable, you can write code that is flexible and can be used in multiple contexts.
