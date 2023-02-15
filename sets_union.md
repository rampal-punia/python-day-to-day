# Union of sets

We use the `union()` method to perform the union operation on two or more sets. The union of two sets A and B is a new set that contains all the elements that are in either A or B, or in both.

The pipe operator `|` is also used for the same purpose in Python sets.

The union() method takes one or more sets as arguments, and returns a new set that contains all the unique elements from the input sets. If there are any duplicates, only one copy is included in the output set.

Both pipe operator `|` and `union()` methods perform the union operation on two sets, which creates a new set containing all the unique elements from both sets.

Here is an example to illustrate the use of the | operator and the union() method:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)

print(set3)  # Output: {1, 2, 3, 4, 5}
```

In this example, we have two sets set1 and set2. We use the union() method to perform the union of the two sets, and store the result in a new set set3. The resulting set set3 contains all the unique elements from both set1 and set2.

The union() method is equivalent to using the | operator to perform the union operation. Here's the same example using the | operator:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1 | set2

print(set3)  # Output: {1, 2, 3, 4, 5}
```

One thing to note is that the | operator has a higher precedence than the union() method, which means that it will be evaluated before the method. For example:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using the | operator with higher precedence
set3 = set1 | set2.intersection({4, 5})
print(set3)  # Output: {3, 4, 5}

# Using the union() method
set4 = set1.union(set2.intersection({4, 5}))
print(set4)  # Output: {3, 4, 5}
```

In this example, we are using the intersection() method to create a new set containing the elements that are common to set2 and the set {4, 5}. We then use the | operator and the union() method to perform the union of set1 and the new set.

Because the | operator has a higher precedence than the union() method, it is evaluated first, and only the common elements between set2 and {4, 5} are added to set1, resulting in the set {3, 4, 5}. If we want to get the union of set1 and the new set, we need to use parentheses to change the order of evaluation:

```python
set5 = set1 | (set2.intersection({4, 5}))
print(set5)  # Output: {1, 2, 3, 4, 5}
```

In general, it's a good practice to use parentheses when using both the | operator and the union() method in the same expression to make the order of evaluation clear.
