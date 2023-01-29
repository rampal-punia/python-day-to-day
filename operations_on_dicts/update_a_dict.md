# Update method of dictionary

The update() method of a dictionary in Python allows you to add new key-value pairs to an existing dictionary. It takes a single argument, which can be another dictionary, a tuple with a pair of two arguments, or any iterable containing key-value pairs.

This method updates the original dictionary in-place and returns None.

Here's an example of how to use the update() method to add a new key-value pair to a dictionary:

```python
# Declare a dictionary
dict1 = {"a": 1, "b": 2, "c": 3}

# Use update() to add a new key-value pair
dict1.update({"d": 4})
print(dict1)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

## Use update to add another dictionary

You can also use the update() method to add multiple key-value pairs from another dictionary.

For example:

```python
# Declare another dictionary
dict2 = {"x": 24, "y": 25, "z": 26}

# Use update() to add all key-value pairs from dict2
dict1.update(dict2)
print(dict1)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'x': 24, 'y': 25, 'z': 26}
```

## Use update to add a a list of tuple(with a pair of two arguments)

You can also use the update() method to add key-value pairs from a list of tuples.

For example:

```python
# Define a list of tuples
letters_wd_numbers = [("d", 4), ("e", 5)]

# Use update() to add key-value pairs from the list of tuples
dict1.update(letters_wd_numbers)
print(dict1)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'x': 24, 'y': 25, 'z': 26, 'd': 4, 'e': 5}
```

Note: If the key is already present in the dictionary, the value will be updated.

Also you can use the update() method with strings it will work like key:value pair.

```python
letters_wd_numbers = ('d4','e5')
dict1.update(letters_wd_numbers)
print(dict1)
# The two values of strings will work as key:value pair.

# Note: the numbers 4 and 5 are of type str here. But you get the idea.
```
