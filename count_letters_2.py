# For more on Python follow: https://twitter.com/CodingMantras


'''✨ Python: Find Most Common Letter in a Sentence.'''

import collections

string_to_count = input("Enter a string: ")

string_to_count = string_to_count.replace(
    ",", "").replace(".", "").replace(" ", "")

counts = collections.Counter(string_to_count.lower())

for letter, count in counts.items():
    print(f"{letter=}, {count=}")
