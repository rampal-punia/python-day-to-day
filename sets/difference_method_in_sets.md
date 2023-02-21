# Difference method in Sets

The `difference()` method is used to get the difference between two or more sets. The method returns a new set containing elements that are in the first set but not in the second set.

The syntax for using the `difference()` method:

```python
set1.difference(set2)
```

For example:

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
diff_set = set1.difference(set2)
print(diff_set)
```

Output:

```python
{1, 2, 3}
```

In the example code, set1 and set2 are two sets containing integers. We then apply the `difference()` method on set1 with set2 as its argument. This returns a new set diff_set that contains elements present in set1 but not in set2.

Note that the difference() method does not modify the original set set1. It creates and returns a new set as a result of the difference operation.

The difference() method can also be used with multiple sets as arguments. In this case, it returns a new set containing elements present in the first set but not in any of the subsequent sets. The syntax for using difference() with multiple sets is as follows:

```python
set1.difference(set2, set3, ...)
```

Additionally, you can use the minus sign (-) operator to find the difference between two sets in Python. The minus sign operator is equivalent to the `difference()` method of the set data type.

For example:

```python
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

diff = set1 - set2

print(diff)  # output: {1, 2}
```

In the example we used the minus sign operator to find the difference between set1 and set2, which resulted in a new set containing the elements that are only in set1 but not in set2. The resulting set is `{1, 2}`.

Both `difference()` method and `-` operator can be used to find the difference between two sets in Python. However, there are some differences in their behavior:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
list1 = [3, 4, 5]

diff = set1.difference(set2)
print(diff)  # Output: {1, 2}

diff = set1.difference(list1)
print(diff)  # Output: {1, 2}

# Using - operator
diff = set1 - set2
print(diff)  # Output: {1, 2}

diff = set1 - list1
print(diff)  # Output: TypeError: unsupported operand type(s) for -: 'set' and 'list'
```

For this behaviour [Python docs says](https://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset):
> Note, the non-operator versions of union(), intersection(), difference(), and symmetric_difference(), issubset(), and issuperset() methods will accept any iterable as an argument. In contrast, their operator based counterparts require their arguments to be sets. This precludes error-prone constructions like set('abc') & 'cbs' in favor of the more readable set('abc').intersection('cbs').

In general, if you just want to find the difference between two sets and don't need to modify any of the sets, using either the difference() method or the - operator is fine.
