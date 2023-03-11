# Python Data-Type Sequence, Collection, Iterable, and Container

Definitions and examples of the terms sequence, collection, iterable, and container in relation to Python data types:

## Sequence

A sequence is an ordered collection of elements. In Python, there are several built-in sequence types, including strings, lists, tuples, and ranges. Here are some examples:

```python
# A string is a sequence of characters
my_string = "hello world"

# A list is a sequence of values
my_list = [1, 2, 3, 4, 5]

# A tuple is an ordered collection of values
my_tuple = ("apple", "banana", "cherry")

# A range is a sequence of numbers
my_range = range(1, 6)
```

## Collection

A collection is a group of related objects. In Python, collections are often implemented as classes that provide additional functionality beyond the built-in types. The collections module in Python provides several useful collection types, including deque, Counter, and defaultdict. Here are some examples

```python
# A deque is a double-ended queue
from collections import deque

my_deque = deque([1, 2, 3, 4, 5])

# Counter is a dictionary subclass for counting occurrences of elements
from collections import Counter

my_list = [1, 2, 3, 3, 3, 4, 5, 5]
my_counter = Counter(my_list)

# defaultdict is a dictionary subclass that provides a default value for nonexistent keys
from collections import defaultdict

my_dict = defaultdict(int)
my_dict["foo"] += 1
```

## Iterable

An iterable is any object that can return an iterator. An iterator is an object that produces the next value in a sequence when next() is called on it. In Python, all sequence types are iterable, as are many other types, such as dictionaries and sets. Here are some examples

```python
# A string is iterable
my_string = "hello world"

for char in my_string:
    print(char)

# A list is iterable
my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)

# A dictionary is iterable (iterating over keys)
my_dict = {"apple": 1, "banana": 2, "cherry": 3}

for key in my_dict:
    print(key)

# A set is iterable
my_set = {1, 2, 3, 4, 5}

for item in my_set:
    print(item)
```

## Container

A container is any object that holds other objects. In Python, containers include lists, tuples, sets, and dictionaries. Here are some examples:

```python
# A list is a container for other objects
my_list = [1, 2, 3, 4, 5]

# A tuple is a container for other objects
my_tuple = ("apple", "banana", "cherry")

# A set is a container for other objects
my_set = {1, 2, 3, 4, 5}

# A dictionary is a container for key-value pairs
my_dict = {"apple": 1, "banana": 2, "cherry": 3}
```

These definitions are not always strictly defined, and some terms may have overlapping meanings in certain contexts. However, understanding these terms can help you choose the appropriate data type for a given task and understand how different types of objects can be used in Python.
