# Discard() Method in Set

In Python, a set is a collection of unique elements. That means if you try to add an element that already exists in the set, it won't be added again. But what if you want to remove an element from the set? That's where the `discard()` method comes in.

The `discard()` method is a built-in method of Python sets that removes an element from the set, if it exists. If the element is not in the set, nothing happens.

For example. Imagine you have a set of programming languages:

```python
prog_languages = {'Python', 'JavaScript', 'Ruby', 'XYZ'}
```

Now let's say you want to remove the element 'XYZ' from the set. You can do that using the discard method like this:

```python
prog_languages.discard('XYZ')
```

After running this code, the set `prog_languages` will contain `{'Python', 'JavaScript', 'Ruby'}`. The 'XYZ' element has been removed from the set.

Now let's say you try to remove an element that doesn't exist in the set. For example, let's try to remove the element 'ABC':

```python
prog_languages.discard('ABC')
```

Since 'ABC' is not in the set, nothing will happen. The set prog_languages will still contain `{'Python', 'Ruby', 'JavaScript'}`.

So in summary, the `discard()` method is a handy way to remove an element from a set if it exists, without raising an error if the element is not in the set.
