# 21 Most Frequently Used Built-in Functions In Python - A Beginners Guide

## Introduction

Python is a popular programming language that is widely used for various purposes such as:

⚡ Software Development
⚡ Web Development
⚡ Desktop GUI Development
⚡ Data Analysis and Visualization
⚡ Predictive Analysis
⚡ Statistics
⚡ Data Science
⚡ Organizing Finances
⚡ Tasks automation
⚡ Games Automation
⚡ Artificial Intelligence / Machine Learning / Deep Learning
⚡ Audio and Video Applications and more...

One of the great things about Python is its extensive library of built-in functions that can make programming tasks easier and more efficient. There are a total of 71 built-in functions in Python.

In this article, we will explore 21 commonly used built-in functions in Python that every beginner should know. These functions are essential for understanding the basics of Python programming and can help you write cleaner, more concise code.

## Table of content

1. print()
2. type()
3. len()
4. id()
5. range()
6. str()
7. list()
8. tuple()
9. dict()
10. input()
11. int()
12. bool()
13. max()
14. min()
15. sum()
16. zip()
17. map()
18. filter()
19. sorted()
20. enumerate()
21. reversed()

### 1. print()

The print() function is used to output text or variables to the console. It can take one or more arguments and it will print each argument separated by a space by default.

Here are some examples:

```python
print("Hello, world!")          
# Output: Hello, world!

print("The answer is", 42)      
# Output: The answer is 42
```

You can also use print() to output variables:

```python
x = "Hello"
y = "world"

print(x, y)    
# Output: Hello world
```

In this example, we define two variables x and y with the strings `"Hello"` and `"world"`, respectively. We then use `print()` to output the values of these variables separated by a space.

You can also use formatting to output variables in a specific format:

```python
name = "John"
age = 30

print("My name is {0} and I am {1} years old.".format(name, age))
# Output: My name is John and I am 30 years old.
```

In this example, we use `print()` to output a string that includes placeholders for the variables name and age. We then use the format() method to substitute the values of these variables into the placeholders.

You can also use f-strings (formatted string literals) to achieve the same result:

```python
name = "John"
age = 30

print(f"My name is {name} and I am {age} years old.")
# Output: My name is John and I am 30 years old.
```

The `print()` function also accepts two optional keyword arguments: sep and end. The sep argument specifies the separator to use between the items being printed, while the end argument specifies the string to append to the end of the output.

Here are some examples:

```python
print("apple", "banana", "orange", sep="-")
# Output: apple-banana-orange
```

We can use `print()` to output two strings on the same line. By default the new line character `\n` is used after the output of each print statement. But we can change this default behavior.

We do this by setting the end argument of the first `print()` call to a space character. This tells `print()` not to append a newline character after the first string is printed. When we call `print()` again on the next line, the output will appear on the same line as the first string.

For example:

```python
print("Hello", end=" ")
print("world!")    

# Output: Hello world!
```

In this example, we use `print()` to output two strings, but we want them to appear on the same line. We do this by setting the end argument of the first `print()` call to a space character. This tells `print()` not to append a newline character after the first string is printed. When we call `print()` again on the next line, the output will appear on the same line as the first string.

### 2. type()

The `type()` function is used to get the data type of an object. It returns the class or type of the object.

Here are some examples:

```python
name = "John"
print(type(name))    
# Output: <class 'str'>

x = 42
print(type(x)) 
# Output: <class 'int'>
```

In first example, we use `type()` to get the data type of the string "John". We store the result in a variable named name. We then use `print()` to output the data type of the string, which is str.

In second example, we use `type()` to get the data type of the number 42. We store the result in a variable named x. We then use `print()` to output the data type of the x, which is int.

```python

numbers = [1, 2, 3, 4, 5]
print(type(numbers))    
# Output: <class 'list'>
```

In this example, we use `type()` to get the data type of a list of numbers. We store the result in a variable named numbers. We then use `print()` to output the data type of the list, which is list.

```python
person = {"name": "John", "age": 30, "city": "New York"}
print(type(person))    
# Output: <class 'dict'>
```

In this example, we use `type()` to get the data type of a dictionary. We store the result in a variable named person. We then use print() to output the data type of the dictionary, which is dict.

**Note**: `type()` can be used with any object in Python. It returns the class or type of the object, regardless of its value or content.

### 3. len()

The `len()` function is used to get the length of an object. The object can be a string, list, tuple, dictionary, or any other iterable. It returns the number of elements in the object.

Here are some examples:

```python
# Find the length of a list
colors = ['Blue', 'Yellow', 'Orange']
print(len(colors))  
# Output: 3

# Find the length of a string
name = "John"
print(len(name))    
# Output: 4

# Find the length of a dictionary
person = {"name": "John", "age": 30, "city": "New York"}
print(len(person))    
# Output: 3
```

**Note**: `len()` can be used with any iterable object. It returns the number of elements in the object, regardless of the data type or content of the object.

### 4. id()

The `id()` function returns the unique identity (integer) of an object. The identity of an object is a unique identifier that remains constant throughout the lifetime of the object, and is guaranteed to be unique among all objects in the system.

Example:

```python
x = 5
print(id(x))  
# Output: 10914496

y = 5
print(id(y))  
# Output: 10914496

z = 6
print(id(z))  
# Output: 10914528
```

In this example, we first assign the integer value 5 to the variable x. When we call the `id()` function on x, we get an integer value of 10914496. We then assign the value 5 to another variable y. When we call `id()` on y, we get the same integer value of `10914496` as we did with x. This indicates that both x and y are referring to the same object in memory.

We then assign the value 6 to the variable z, and when we call `id()` on z, we get a different integer value of `10914528`. This indicates that z is referring to a different object in memory than x and y.

The `id()` function is often used in conjunction with the is keyword to compare the memory locations of two objects.

Example:

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(id(a))  # Output: 140603319251264
print(id(b))  # Output: 140603319251264
print(id(c))  # Output: 140603319251136

print(a is b)  # Output: True
print(a is c)  # Output: False
```

In this example, we use the `id()` function to print out the memory location of a, b, and c. We can see that a and b have the same memory location, while c has a different memory location.

We then use the is keyword to compare a and b, which returns True since they have the same memory location. We also compare a and c using is, which returns False since they have different memory locations.

### 5. range()

The `range()` function is a built-in function that is used to generate a sequence of numbers. It takes up to three arguments: `start`, `stop`, and `step`. The `start` argument specifies the starting point of the sequence, `stop` argument specifies the ending point of the sequence (exclusive), and `step` specifies the difference between each number in the sequence. If `start` is not specified, it defaults to 0. If `step` is not specified, it defaults to 1.

Here's an example of using the `range()` function to generate a sequence of numbers:

```python
for i in range(10):
    print(i, end=" ")

# Output: 0 1 2 3 4 5 6 7 8 9
```

In the example above, we use the `range()` function to generate a sequence of numbers from 0 to 9, and then we use a for loop to iterate over the sequence and print each number.

We can also specify the starting and ending points of the sequence, as well as the step size, like this:

```python
for i in range(0, 20, 2):
    print(i, end=" ")

# Output: 0 2 4 6 8 10 12 14 16 18
```

In this example, we use the `range()` function to generate a sequence of even numbers from 2 to 10 with a step of 2, and then we use a for loop to iterate over the sequence and print each number.

If the `step` argument is negative, `start` should be greater than `stop` for the sequence to be non-empty:

```python
# Generate a sequence of numbers from 10 to 1 (descending order)
for i in range(10, 0, -1):
    print(i, end=' ')

# Output:
10 9 8 7 6 5 4 3 2 1
```

### 6. str()

In Python, the `str()` function is used to convert a given value to a string.

Here are some examples:

```python
# integer to string
x = str(42)
print(x)    # Output: "42"

# float to string
y = str(3.14)
print(y)    # Output: "3.14"

# bool to string
z = str(True)
print(z)    # Output: "True"
```

**Note**: `str()` can be used to convert values of various data types to strings, including integers, floating-point numbers, and boolean values. When converting a boolean value to a string, the resulting string will be either "True" or "False".

### 7. list()

The `list()` is a built-in function that creates a new list object. It can take an iterable object as an argument and convert it into a list. A list is a collection of ordered and mutable elements enclosed in square brackets.

Here's an example of how to use `list()` function:

```python
# Example 1: Creating a list using the list() function
numbers = list(range(1, 6))   # creating a list from a range object
print(numbers)   
# output: [1, 2, 3, 4, 5]

fruits = list(('apple', 'banana', 'cherry'))  # creating a list from a tuple
print(fruits)   
# output: ['apple', 'banana', 'cherry']
```

In the example above, we used the `list()` function to create a list from a range object and a tuple.

### 8. tuple()

The `tuple()` function is used to create a tuple object from an iterable or a sequence. Tuples are similar to lists, but they are immutable, meaning that they cannot be modified once created.

The `tuple()` function takes an iterable as an argument and returns a tuple object. If the argument is already a tuple, it returns a copy of the same tuple.

Here is an example code demonstrating the use of `tuple()` function:

```python
# create a list of numbers
numbers = [1, 2, 3, 4, 5]

# create a tuple from the list using tuple() function
tuple_numbers = tuple(numbers)

print(tuple_numbers)  
# Output: (1, 2, 3, 4, 5)

# create a tuple directly from elements using tuple() function
tuple_letters = tuple('Hello World')

print(tuple_letters)  
# Output: ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')

# create a tuple from a range of numbers using tuple() function
tuple_range = tuple(range(1, 6))

print(tuple_range)  
# Output: (1, 2, 3, 4, 5)
```

In the example above, we created a list of numbers and then used the `tuple()` function to convert it into a tuple. We also created a tuple directly from elements and used the `tuple()` function to create a tuple from a range of numbers.

Tuples are useful when you need to store a sequence of values that won't change. They are faster and consume less memory than lists.

### 9. dict()

The `dict()` function is used to create a new dictionary object or convert an iterable of key-value pairs into a dictionary. It returns a new dictionary object.

The syntax for using the `dict()` function is as follows:

```python
dict()
dict(mapping)
dict(iterable)
dict(**kwargs)
```

where mapping can be a dictionary or an object that supports the `dict()` constructor and iterable is an iterable object containing key-value pairs.

Here are some examples to demonstrate the use of `dict()` function:

Example 1: Creating a dictionary using `dict()`

```python
# Creating an empty dictionary
my_dict = dict()
print(my_dict)  
# Output: {}

# Creating a dictionary with initial values
my_dict = dict(a=1, b=2, c=3)
print(my_dict)  
# Output: {'a': 1, 'b': 2, 'c': 3}

# Creating a dictionary from a list of tuples
my_dict = dict([('a', 1), ('b', 2), ('c', 3)])
print(my_dict)  
# Output: {'a': 1, 'b': 2, 'c': 3}
```

In the first example, we create an empty dictionary using `dict()`. In the second example, we create a dictionary with initial values by passing keyword arguments to `dict()`. In the third example, we create a dictionary from a list of tuples.

Example 2: Converting an iterable into a dictionary using `dict()`

```python
# Converting a list of lists into a dictionary
my_list = [['a', 1], ['b', 2], ['c', 3]]
my_dict = dict(my_list)
print(my_dict)  
# Output: {'a': 1, 'b': 2, 'c': 3}

# Converting a list of tuples into a dictionary
my_list = [('one', 1), ('two', 2), ('three', 3)]
my_dict = dict(my_list)
print(my_dict)  
# Output: {'one': 1, 'two': 2, 'three': 3}

# Converting a string into a dictionary
my_str = "{'a': 1, 'b': 2, 'c': 3}"
my_dict = dict(eval(my_str))
print(my_dict)  
# Output: {'a': 1, 'b': 2, 'c': 3}
```

In the first example, we convert a list of tuples into a dictionary. In the second example, we convert a list of lists into a dictionary. In the third example, we convert a string representation of a dictionary into a dictionary using the `eval()` function.

Example 3: Using `**kwargs` to create a dictionary

```python
# Creating a dictionary using **kwargs
my_dict = dict(a=1, b=2, c=3, **{'d': 4, 'e': 5})
print(my_dict)  
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

In this example, we use `**kwargs` to create a dictionary by passing a dictionary as a keyword argument.

### 10. input()

The `input()` function is used to get input from the user via the console. It prompts the user to enter some data and waits for them to provide it. The `input()` function returns the user's input as a **string**.

Here are some examples:

```python
name = input("What's your name?: ")
print(f"Hello, {name.capitalize()}!")


# In terminal
What's your name?: <john>
# Output: Hello, John!
```

You can also convert the user's input to a different data type using type casting:

```python
age = int(input("How old are you?: "))
print("You will be " + str(age + 1) + " years old next year.")    

# Output: You will be <age + 1> years old next year.
```

In this example, we use `input()` to prompt the user to enter their age. We then convert their input to an integer using the `int()` function. We store the user's age in the variable age. We then use `print()` to output a message that includes the user's age incremented by 1.

**Note**: `input()` always returns a string, so we have to use type casting to convert it to a different data type if needed.

You can also use `input()` in a loop to get multiple inputs from the user:

```python
numbers = []
for i in range(3):
    num = int(input("Enter a number: "))
    numbers.append(num)
print("The sum of the numbers is:", sum(numbers))

# Output: The sum of the numbers is: <sum>
```

In this example, we use `input()` in a loop to get three integers from the user. We convert each input to an integer using the int() function and append it to the list numbers. We then use sum() to calculate the sum of the numbers and output it using print().

Suppose, you are writing a program to asking for person's age. You can validate the user_input to get only integer value in a range of 0-125, using try-except block.

```python
def validate_input(user_input):
    try:
        user_input = int(user_input)
        if user_input < 1 or user_input > 125:
            raise ValueError("Number must be between 1 and 125")
        return user_input
    except ValueError:
        return False
```

### 11. int()

The `int()` function is used to convert a given value to an integer.

So, it converts a number or string to an integer, or return 0 if no arguments are given. If x is a number, return integer value of x. For floating point numbers, this truncates towards zero.

```python
# floating point number to integer
x = int(4.9)
print(x)
# Output: 4

# string to integer
x = "40"
print(int(x, base=10))
# Output: 40

# boolean is a subset of type int
z = int(True)
print(z)
# Output: 1
```

**Note**: int() can be used to convert values of various data types to integers, including floating-point numbers, strings, and boolean values. When converting a string to an integer, the string must contain only numeric characters. If the string contains non-numeric characters, a ValueError will be raised.

### 12. bool()

The bool() function is used to convert a value to a boolean value. It returns True if the value is considered to be true, and False if the value is considered to be false.

Here are some examples:

```python
print(bool(5))          # True
print(bool('hello'))    # True
print(bool([1,2,3]))    # True

print(bool(0))          # False
print(bool(''))         # False
print(bool([]))         # False
print(bool(None))       # False
```

### 13. max()

In Python, the `max()` function is used to get the maximum value from a sequence (list, tuple, or set).

Here are some examples:

```python
x = [1, 2, 3, 4, 5]
y = max(x)
print(y)    
# Output: 5

x = (1.5, 2.5, 3.5)
y = max(x)
print(y)    
# Output: 3.5

x = {1, 3, 5, 7}
y = max(x)
print(y)    
# Output: 7
```

How to find the word with maximum length from a list of words.  

The `max()` function accepts a keyword-only argument key. We can pass a function to the key argument, and `max()` will compare the elements of a list based on the value returned by this function.

```python
words = ['apple', 'banana', 'pineapple', 'cherry', 'date']
max_word = max(words, key=len)

print("Word with maximum length:", max_word)

# Output: Word with maximum length: pineapple
```

In the example above, the `max()` function is called with the key parameter set to the built-in function len(). This tells `max()` to compare the elements of the words list based on their lengths, and return the maximum element based on this criterion.

The max_word variable then stores the word with maximum length, which is printed to the console using the print() function.

**Note**: `max()` only works on sequences that contain comparable values. If you try to use `max()` on a sequence that contains non-comparable values, such as a mix of integers and strings, you will get a TypeError.

### 14. min()

The `min()` function is used to get the minimum value from a sequence (list, tuple, or set).

Here are some examples:

```python
x = [1, 2, 3, 4, 5]
y = min(x)
print(y)
# Output: 1

x = (1.5, 2.5, 3.5)
y = min(x)
print(y)
# Output: 1.5

x = {1, 3, 5, 7}
y = min(x)
print(y)
# Output: 1
```

The min function also accepts the keyword only argument `key`, which can be used in the similar way as discussed for `max()` function.

**Note**: `min()` only works on sequences that contain comparable values. If you try to use `min()` on a sequence that contains non-comparable values, such as a mix of integers and strings, you will get a TypeError.

### 15. sum()

In Python, the `sum()` function is used to get the sum of all the elements in a sequence (list, tuple, or set).

Here are some examples:

```python
# Sum of integer values
x = [1, 2, 3, 4, 5]
y = sum(x)
print(y)    # Output: 15

# Sum of floating-point numbers
x = (1.5, 2.5, 3.5)
y = sum(x)
print(y)    # Output: 7.5

# sum of set 'x'
x = {1, 3, 5, 7}
y = sum(x)
print(y)    # Output: 16
```

**Note**: `sum()` only works on sequences that contain numeric values, such as integers or floating-point numbers. If you try to use `sum()` on a sequence that contains non-numeric values, such as strings or booleans, you will get a TypeError.

### 16. zip()

The `zip()` function is used to combine two or more iterables into a single iterable. It takes two or more iterables as arguments and returns an iterator that generates a series of tuples, where the i-th tuple contains the i-th element from each of the input iterables.

Example 1: Combining two lists into a single list of tuples

```python
# Example 1: Combining two lists of equal lengths
colors = ['Yellow', 'Blue', 'Orange']

hex_values = ['#FFFF00', '#0000FF', '#FFA500']

for color, hex_value in zip(colors, hex_values):
    print(color, hex_value)
# Output:
# Yellow  # FFFF00
# Blue  # 0000FF
# Orange  # FFA500
```

If the iterables passed to `zip()` have different lengths, the resulting iterable will have the length of the shortest iterable.

Example:

```python
# example 2: Combining two lists of different lengths
numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(list(zipped))   # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
```

We can also use `zip()` with more than two iterables:

for example:

```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]

result = zip(list1, list2, list3)

print(list(result))  

# Output: [(1, 'a', True), (2, 'b', False), (3, 'c', True)]
```

### 17. map()

The `map()` function applies a given function to each item of an iterable (e.g., list, tuple) and returns a new iterable with the results.

Here's an example code to illustrate the use of `map()`:

```python
# Define a function to be applied to each element of the list
def square(x):
    return x**2

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() to apply the function to each element of the list
squared_numbers = map(square, numbers)

# Print the original and the squared numbers
print("Original numbers:", numbers)
print("Squared numbers:", list(squared_numbers))
```

In this example, we define a function `square()` that takes a number as an input and returns its square. We also define a list numbers containing some integers.

We then use `map()` to apply the `square()` function to each element of the numbers list. The result is a new iterable containing the squared numbers.

We convert the squared_numbers iterable to a list using the `list()` function and print both the original and the squared numbers.

Output:

```bash
Original numbers: [1, 2, 3, 4, 5]
Squared numbers: [1, 4, 9, 16, 25]
```

**Note**: `map()` returns an iterator, which can be converted to a list, tuple, or other iterable. The function passed to `map()` must take exactly one argument. If the function requires multiple arguments, you can use the lambda function or functools.partial() to create a function with the correct number of arguments.

If there are multiple iterables passed as arguments to `map()`, then the function passed to `map()` should have as many arguments as there are iterables, and it will be applied to the corresponding items of each iterable.

For example:

```python
# Define two lists
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30, 40, 50]

# Use map() to add the corresponding numbers from both lists
sums = map(lambda x, y: x + y, numbers1, numbers2)

# Print the sums
print(list(sums))

# Output: [11, 22, 33, 44, 55]
```

Here, we define two lists numbers1 and numbers2. We then use map() to add the corresponding elements of both lists using a lambda function. The result is a new iterable containing the sums. We convert the iterable to a list using the `list()` function and print it.

### 18. filter()

The `filter()` function is used to filter out elements from a sequence that don't satisfy certain conditions, based on a given function. The output of this function is a filter object, which can be converted to a list or other iterable type for further processing.

The general syntax for using the `filter()` function is as follows:

```bash
filter(function, sequence)
```

Here, function is a function that returns a Boolean value and sequence is the iterable sequence that is to be filtered. The `filter()` function applies the function to each element of the sequence and returns only those elements for which the function returns True.

Let's see an example of using the `filter()` function:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(num):
    return num % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(even_numbers)
```

In this example, we define a list of numbers from 1 to 10. We also define a function `is_even()` that returns True if a number is even and False otherwise. We then use the `filter()` function to filter out the even numbers from the list using the `is_even()` function. Finally, we convert the filter object to a list and print the resulting list of even numbers.

The output of this program would be:

```bash
[2, 4, 6, 8, 10]
```

When we passed the `is_even()` function as the first argument to the `filter()` function. The `filter()` function then applied the `is_even()` function to each element of the numbers list and returned only those elements for which the function returned True, i.e., the even numbers.

If the function argument is None, then the `filter()` function simply returns the elements of the sequence that are considered true, based on their Boolean value.

Now let's see an example of using the `filter()` function with lambda function:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
```

In this example, we use a lambda function to define the condition for filtering out even numbers from the numbers list. The `filter()` function then applies this lambda function to each element of the numbers list and returns only those elements for which the function returns True.

The output of this program would be the same as the previous example:

```bash
[2, 4, 6, 8, 10]
```

If the two iterables are not of equal length, then the `filter()` function returns the filtered elements only up to the length of the shortest iterable.

### 19. sorted()

The `sorted()` function is used to sort a sequence (list, tuple, or string) in ascending order.

Here are some examples:

```python
# sorting a list alphabetically
colors = ['Yellow', 'Blue', 'Orange']
print(sorted(colors))
# Output: ['Blue', 'Orange', 'Yellow']

# numerical sorting
x = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
y = sorted(x)
print(y)
# Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# sorting a string alphabetically
x = "hello, world!"
y = sorted(x)
print(y)
# Output: [' ', '!', ',', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
```

**Note**: `sorted()` does not modify the original sequence; it creates a new sorted sequence. Also note that `sorted()` works on any sequence type, not just lists.

### 20. enumerate()

The `enumerate()` function is used to add a counter to an iterable and return it as an enumerate object. This function is very useful when we need to keep track of the index of the elements in the iterable.

The `enumerate()` function takes an iterable as input and returns a tuple with two elements: the index of the element, and the element itself.

Here's an example of how to use the `enumerate()` function:

```python
fruits = ['apple', 'banana', 'kiwi', 'mango']

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output:
0 apple
1 banana
2 kiwi
3 mango
```

In the example above, we have a list of fruits, and we are using the `enumerate()` function to iterate over the list and print out each element along with its index. We are unpacking the tuple returned by the `enumerate()` function into two variables, index and fruit. The variable index holds the index of the current element in the iteration, and the variable fruit holds the current element itself.

We can also specify the starting value of the index by passing it as the second argument to the `enumerate()` function.

Here's an example:

```python
fruits = ['apple', 'banana', 'kiwi', 'mango']

for index, fruit in enumerate(fruits, start=101):
    print(index, fruit)

# Output:
101 apple
102 banana
103 kiwi
104 mango
```

In the example above, we have specified the starting value of the index as 101 by passing start=101 as the second argument to the `enumerate()` function. The output shows that the index of the first element is 101 instead of the default value of 0.

We can also convert the `enumerate()` object to a list of tuples using the `list()` function. Here's an example:

```python
fruits = ['apple', 'banana', 'kiwi', 'mango']
enum_fruits = list(enumerate(fruits))

print(enum_fruits)

# Output:
[(0, 'apple'), (1, 'banana'), (2, 'kiwi'), (3, 'mango')]
```

In the example above, we have converted the `enumerate()` object to a list of tuples using the `list()` function. The output shows that each tuple contains the index of the element as the first element and the element itself as the second element.

### 21. reversed()

The reversed() function is used to return a reverse iterator over a sequence. It accepts a single argument that must be a sequence, such as a list, tuple, or string, and returns an iterator that generates the elements of the sequence in reverse order.

Here's an example:

```python
my_list = [1, 2, 3, 4, 5]
for num in reversed(my_list):
    print(num)

# Output
5
4
3
2
1
```

In this example, we have a list my_list containing five elements. We use the `reversed()` function to create a reverse iterator over the list. Then we loop through the iterator using a for loop and print each element in reverse order.

We can also convert the iterator to a list, tuple or string using the respective constructor functions. Here are some examples:

```python
my_tuple = (1, 2, 3, 4, 5)
reversed_tuple = tuple(reversed(my_tuple))
print(reversed_tuple)  
# Output: (5, 4, 3, 2, 1)

my_string = "hello"
reversed_string = "".join(reversed(my_string))
print(reversed_string)  
# Output: "olleh"
```

In these examples, we use the `reversed()` function to create a reverse iterator over a tuple and a string, respectively. We then use the tuple() and "".join() functions to convert the iterator to a tuple and a string, respectively, with the elements in reverse order.

**Note**: the `reversed()` function does not modify the original sequence, but rather returns a new iterator object that generates the elements in reverse order.

## Conclusion

In conclusion, the built-in functions in Python are a powerful tool that can help beginners write better code and work more efficiently.

In this article, we covered 21 commonly used built-in functions that every beginner should know. By using these functions in your code, you can make your programs more concise, readable, and efficient. By mastering these functions, you will be well on your way to becoming a proficient Python programmer.
