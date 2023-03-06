# isdisjoint method of in Python sets

The isdisjoint() method is a built-in function that can be used to determine whether two sets have any common elements. The method returns `True` if the sets have no common elements, and `False` otherwise. In other words, this method returns `True` if two sets have a null intersection.

Here is the syntax for the `isdisjoint()` method:

```python
set1.isdisjoint(set2)
```

where set1 and set2 are the two sets being compared.

The `isdisjoint()` method takes only one argument, which must be an iterable. The `isdisjoint()` method can be used to check for common elements between two sets. For example, suppose we have two sets:

```python
set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}
```

We can use the `isdisjoint()` method to determine if there are any common elements between them:

```python
set1.isdisjoint(set2)
True
```

Since there are no common elements between set1 and set2, the `isdisjoint()` method returns True.

Now let's consider another example:

```python
set3 = {3, 4, 5, 6}
```

We can use the `isdisjoint()` method to check for common elements between set1 and set3:

```python
set1.isdisjoint(set3)
False
```

Since set1 and set3 share elements 3 and 4, the `isdisjoint()` method returns False.

If the argument passed to the `isdisjoint()` method is not an iterable, a `TypeError` will be raised. It is worth noting that this method works for any iterable object, not just sets.

```python
set1 = {1, 2, 3, 4}
num = 5

print(set1.isdisjoint(num))
# TypeError: 'int' object is not iterable
```

It will work for a tuple or list. For example:

```python
s = {1, 2, 3, 4}
l = [5, 6, 7, 8]
t = (4, 5, 6, 7)

print(s.isdisjoint(l))   # True
print(s.isdisjoint(t))   # False
```

The `isdisjoint()` method can be useful in a variety of situations, such as checking if two lists have any common elements by first converting them to sets.
