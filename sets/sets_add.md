# `add()` method in sets

In Python, a set is an unordered collection with no duplicate elements.

The basic uses of set include membership testing and eliminating duplicate entries. Sets have an `add()` method to add elements to the set.

## Syntax

```python
s.add(element)
```

The add method modifies the set in place and does not return anything. If the element is already in the set, the add method has no effect. If the element is not in the set, it is added to the set.

For example:

```python
# Create a set
s = set([1, 2, 3])

# Or
s = {1, 2, 3}

# Add an element to the set
s.add(4)

# Add an element that is already in the set
s.add(2)

# Print the set
print(s)
```

In this example, the set `s` is created with the elements 1, 2, and 3. The add method is used to add element 4 to the set. The add method is also used to add element 2 to the set, but since 2 is already in the set, the add method has no effect.

Finally, the set is printed, and the output is:

```bash
{1, 2, 3, 4}
```

So the add method of sets in Python is a simple method that adds an element to a set if the element is not already in the set.
