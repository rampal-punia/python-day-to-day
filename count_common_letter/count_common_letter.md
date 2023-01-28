# Count Common Letter In A String

To count the most common letter appeared in a given string, we can use the `Counter` class from the `collections` module.

For example:

```python
'''✨ Python: Find Most Common Letter in a Sentence.'''

import collections

string_to_count = "I love learning Python a Lot"

counts = collections.Counter(string_to_count.lower())
print(f"{counts=}")
```

Output of the code:

```bash
counts=Counter({' ': 5, 'l': 3, 'o': 3, 'n': 3, 'i': 2, 'e': 2, 'a': 2, 't': 2, 'v': 1, 'r': 1, 'g': 1, 'p': 1, 'y': 1, 'h': 1})
```

## Get most common 3 letters

We can find the moost common 3 letters using the `most_common()` method. This method returns **a List with the n most common elements and their counts from the most common to the least. If n is None, then list all element counts**.

For example:

```python
import collections

string_to_count = "I love learning Python a Lot"

counts = collections.Counter(string_to_count.lower())
print(f"{counts=}")

# # Print most common 3 letters from the given string.
print(f"Most common 3 letters are: {counts.most_common(3)}")
```

Output:

```bash
counts=Counter({' ': 5, 'l': 3, 'o': 3, 'n': 3, 'i': 2, 'e': 2, 'a': 2, 't': 2, 'v': 1, 'r': 1, 'g': 1, 'p': 1, 'y': 1, 'h': 1})
Most common 3 letters are: [(' ', 5), ('l', 3), ('o', 3)]
```

## Sort the List Alphabetically

```python
import collections

string_to_count = "I love learning Python a Lot"

counts = collections.Counter(string_to_count.lower())
print(f"{counts=}")

# # Print most common 3 letters from the given string.
print(f"Most common 3 letters are: {counts.most_common(3)}")


# Sort the list alphabetically
sorted_list = {k: v for k, v in sorted(
    counts.items(), key=lambda item: item[0])}
print(f"{sorted_list=}")
```

## Improve the code

- We can ask the string as an input from the user and give back the letters-count and most common letter to the user.

- The output format of the Counter object is not very readable, you could use the items() method of the Counter object to print the counts in a more readable format.

For example:

```python
'''✨ Python: Find Most Common Letter in a Sentence.'''

import collections

string_to_count = input("Enter a string: ")

string_to_count = string_to_count.replace(
    ",", "").replace(".", "").replace(" ", "")

counts = collections.Counter(string_to_count.lower())

for letter, count in counts.items():
    print(f"{letter=}, {count=}")
```
