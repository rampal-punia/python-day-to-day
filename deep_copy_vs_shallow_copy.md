# Deep copy Vs Shallow copy in Python

In Python, when we make a copy of an object, there are two types of copying available: shallow copy and deep copy. The fundamental difference between the two types of copies is how the objects are referenced.

Understanding the difference between these two is important, as it can affect the behavior of our programs.

## Shallow Copy

A shallow copy creates a new object but does not duplicate the mutable objects inside the original object. Instead, the new object will reference the same mutable objects as the original object. Changes made to these mutable objects will affect both the original and copied objects. We can use the copy() method to create a shallow copy of an object. Here's an example:

```python
original_list = [1, 2, 3, [4, 5]]
shallow_copy = original_list.copy()

original_list[3].append(6)

print(original_list)
# Output : [1, 2, 3, [4, 5, 6]]

print(shallow_copy)
# Output : [1, 2, 3, [4, 5, 6]]
```

In the above example, we have a list `original_list` with four elements, one of which is a nested list. We create a shallow copy of original_list using the `copy()` method and assign it to `shallow_copy`. Then we modify the nested list of `original_list` by appending a new element to it. When we print both `original_list` and `shallow_copy`, we can see that they both have the same changes. This is because the shallow copy references the same memory locations as the original list.

## Deep Copy

A deep copy, on the other hand, creates a new object and recursively copies all the mutable objects inside the original object. A deep copy is an entirely new object that is identical to the original object. This means that changes made to the mutable objects in the copied object will not affect the original object, and vice versa. We can use the `deepcopy()` method from the copy module to create a deep copy of an object. Here's an example:

Here is an example:

```python
import copy

original_list = [1, 2, 3, [4, 5]]
deep_copy = copy.deepcopy(original_list)

original_list[3].append(6)

print(original_list)
# Output: [1, 2, 3, [4, 5, 6]]
print(deep_copy)
# Output: [1, 2, 3, [4, 5]]
```

In the above example, we use the `deepcopy()` method from the copy module to create a deep copy of `original_list` and assign it to `deep_copy`. Then we modify the nested list of `original_list` by appending a new element to it. When we print both `original_list` and `deep_copy`, we can see that `deep_copy` remains unchanged, as it is an entirely new object that is independent of the original list.

In summary, the main difference between a shallow copy and a deep copy is how the objects are referenced. A shallow copy references the same memory locations as the original object, while a deep copy creates an entirely new object that is independent of the original object.

In Python, everything is an object. Like range object, list object, map object so on...

An enumerate object is an iterator that assigns an index to each item in an iterable object, such as a list or tuple. (In our case languages list)

It's a built-in function that allows you to loop over an iterable and keep track of the index of the current item.

The enumerate function returns an enumerate object, which contains pairs of index and corresponding value from the iterable.

We can use the enumerate object to access the items and their index simultaneously in a for loop.
