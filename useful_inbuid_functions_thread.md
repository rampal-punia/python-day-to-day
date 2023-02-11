# 21 Commonly used in-built functions In Python with example code

print():
Output text or variables to the console

Ex:

```python
print("Hello, World!")
```

input():
Reads a line of text from the user and returns it as a string

Ex:

```python
name = input("What's your name? ")
print(f"Hello, {name}!")
```

len():
Returns the number of items in a list, string, or other data structure

Ex:

```python
colors = ['Blue', 'Yellow', 'Orange']
print(len(colors))  # Output: 3
```

type():
Returns the type of an object, such as int, float, list, etc

Ex:

```python
x = 42
print(type(x)) # Output: <class 'int'>
```

int():
Convert a number or string to an integer, or return 0 if no arguments are given. If x is a number, return x.__int__(). For floating point numbers, this truncates towards zero.
Ex:

```python
x = "40"
print(int(x, base=10))
```

float():
Convert a string or number to a floating point number, if possible(Correct Input).

Ex:

```python
x = "42"
print(float(x))
```

str():
Create a new string object from the given object.

Ex:

```python
x = 42
print(str(x))
```

sorted():
Sorts a list or other iterable object in ascending or descending order

Ex:

```python
colors = ['Yellow', 'Blue', 'Orange']
print(sorted(colors))

# ['Blue', 'Orange', 'Yellow']
```

sum():

Returns the sum of all elements in an iterable object, such as a list or tuple

Ex:

```python
numbers = [1, 2, 3, 4, 5]
print(sum(numbers)) # Output: 15
```

max():
With a single iterable argument, return its biggest item.

Ex:

```python
numbers = [1, 2, 3, 4, 5]
print(max(numbers)) # Output: 5
```

min():
With a single iterable argument, return its smallest item.

Ex:

```python
numbers = [1, 2, 3, 4, 5]
print(min(numbers)) # Output: 1
```

abs():
Returns the absolute value of a number

Ex:

```python
x = -42
print(abs(x)) # Output: 42
```

round():
Rounds a floating-point number to the nearest integer or to a specified number of decimal places

Ex:

```python
x = 3.14159
print(round(x)) # Output: 3
print(round(x, 2)) # Output: 3.14
```

zip():
Combines elements from multiple iterables into a single tuple

Ex:

```python
colors = ['Yellow', 'Blue', 'Orange']

hex_values = ['#FFFF00', '#0000FF', '#FFA500']

for color, hex_value in zip(colors, hex_values):
    print(color, hex_value)
# Output:
# Yellow  # FFFF00
# Blue  # 0000FF
# Orange  # FFA500
```

map():
Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.

Ex:

```python
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(squared) # Output: [1, 4, 9, 16, 25]
```

filter():

Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true.

Ex:

```python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
evens = list(filter(is_even, numbers))
print(evens) # Output: [2, 4]
```

enumerate():
Returns an iterator containing pairs of the form (index, element)` for each element in an iterable

Ex:

```python
colors = ['Yellow', 'Blue', 'Orange']
for i, color in enumerate(colors):
    print(i, color)
# Output:
# 0 apple
# 1 banana
# 2 cherry
```

range():
Generates a sequence of integers, which can be used to control the number of iterations in a loop

Ex:

```python
for i in range(1, 100, 2):
    print(i)
```

reversed():
Returns a reverse iterator over the elements of a sequence, such as a list or a string

Ex:

```python
colors = ['Yellow', 'Blue', 'Orange']
for color in reversed(colors):
    print(color)
```

help():
Display the documentation or help for a specific object, such as a module, class, function, or method. It provides information about the object's syntax, parameters, return value, and other details

Ex:

```python
help("def")
```

dir():
Return a list of the names of all attributes, methods, and properties of an object. This includes built-in attributes and methods, as well as any that have been dynamically added to the object

Ex:

```python
dir(list)
```
