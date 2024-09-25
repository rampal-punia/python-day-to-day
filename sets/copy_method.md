# Copy method in Python Sets

The `copy()` method is a built-in set method that returns a shallow copy of the set.

## Syntax

```python
s.copy()
```

## How does the `copy()` method work?

### Creates a new empty set

The `copy()` method creates a new empty set that will be used to store the copied elements.

### Iterates over the original set

The `copy()` method then iterates over each element in the original set and adds it to the new set (Add the reference to that element).

### Return the new set

Once all elements have been copied, the `copy()` method returns the new set.

For example:

```python
# create a set of numbers
original_set = {1, 2, 3, 4, 5}

# create a copy of the set using the copy() method
copied_set = original_set.copy()

# Add a new number to the original set
original_set.add(6)

# Print both sets to see the difference
print(original_set) # Output: {1, 2, 3, 4, 5, 6}
print(copied_set)   # Output: {1, 2, 3, 4, 5}
```

Here, We create a set of numbers `original_set` and then create a copy of the set `copied_set` using the `copy()` method. We then add a new number to the original set and print both sets to see the difference. We can see, the original set has the additional element, while the copied set remains unchanged.

Note: The `copy()` method creates a shallow copy of the set, which means that the elements themselves are not copied. Instead, both the original set and the copied set will reference the same objects.

An example to demonstrate that the ID of the original set and the copied set are different but the ids of the elements are same:

```python
# create a set of numbers
original_set = {1, 2, 3, 4, 5}

# create a copy of the set using the copy() method
copied_set = original_set.copy()

# print the IDs of the original set and the copied set
print("Original set id:", id(original_set))
print("Copied set id:", id(copied_set))
# Original set id: 140113763621792
# Copied set id: 140113764694944

# print the IDs of the original & copied elements
print("Original set element ids:", [id(x) for x in original_set])
print("Copied set element ids:", [id(x) for x in copied_set])
# Original set element ids: [9793088, 9793120, 9793152, 9793184, 9793216]
# Copied set element ids: [9793088, 9793120, 9793152, 9793184, 9793216]
```

The ID of the original set and the copied set are different, we use the built-in id() function to print the IDs of both sets. As you can see from the output, the IDs of the original set and the copied set are different, which confirms that they are distinct objects in memory. The ids of the `original_set` elements are the same as the ids of the `copied_set` elements. Which means both the sets reference to the same elements in the memory.

## A few things to keep in mind while using the `copy()` method for sets in Python

### Shallow copy

The `copy()` method creates a shallow copy of the set.

### Performance

The `copy()` method can be slower than creating a new set from scratch. This is because the method needs to iterate over each element in the original set and add it to the new set. If the set is large, this can be a time-consuming process.

### Memory usage

If you create a copy of a large set using the `copy()` method, it will consume additional memory in your program. This can be a concern if memory usage is a critical factor in your application.

### Immutable objects

If the set only contains immutable objects, such as integers or strings, then using the `copy()` method should not cause any issues. Since these objects cannot be modified, there is no risk of unexpected behavior due to shared references.

## Other ways to achieve the same functionality as the `copy()` method in sets

### Set constructor

You can use the set constructor to create a new set that is a copy of an existing set. For example:

```python
original_set = {1, 2, 3}
new_set = set(original_set)
```

This will create a new set new_set that contains the same elements as original_set.

### Set union

You can use the set union operator (|) to combine two sets into a new set. For example:

```python
original_set = {1, 2, 3}
new_set = original_set | set()
```

This will create a new empty set using the set() constructor and then combine it with the original_set using the | operator, resulting in a new set new_set that is a copy of original_set.

### Unpacking operator (*)

This will create a new set new_set that contains the same elements as original_set. The unpacking operator (*) is used to pass the elements of the original_set to `{}`, which creates a new set with the same elements.

```python
original_set = {1, 2, 3}
new_set = {*original_set}
```

All of these approaches will create a new set that is a copy of the original set, without modifying the original set.
