# Difference between the Discard, Remove and Pop method in Python Sets

In Python, sets are unordered collections of unique elements. They are mutable, which means that elements can be added or removed from the set. There are three methods to remove elements from a set: pop(), discard() and remove(). Although all three methods remove elements from a set, they have different functionalities and return values. Let's take a closer look at each of these methods.

## Pop()

The pop() method removes an arbitrary element from the set and returns it. If the set is empty, a KeyError is raised. The order in which the elements are removed is not guaranteed, as sets are unordered. Here's an example:

```python
fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(x)
print(fruits)
```

Output:

```python
cherry
{'banana', 'apple'}
```

## discard()

The discard() method removes a specified element from the set if it is present. If the element is not present, the method does nothing. Unlike the pop() method, discard() does not raise an error if the element is not present. Here's an example:
``python
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

```
Output:
```bash
{'cherry', 'apple'}
```

## remove()

The remove() method removes a specified element from the set if it is present. If the element is not present, a KeyError is raised. Here's an example:

```python
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)
```

Output:

```bash
{'cherry', 'apple'}
```

To summarize, pop() removes an arbitrary element from the set and returns it, discard() removes a specified element from the set if it is present, and remove() removes a specified element from the set and raises a KeyError if the element is not present. It is important to choose the right method depending on the requirements of your program.
