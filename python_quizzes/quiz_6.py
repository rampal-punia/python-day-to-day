'''✨ Python Quiz ✨ 

What would be the output:
A) {1: 'Ruby', 3.0: 'Rust', 3: 'Python'}
B) {1: 'Ruby', 3.0: 'Rust'}
C) {1: 'Ruby', 3.0: 'Python'}
D) Error
'''
languages = {}
languages[1] = "Ruby"
languages[3.0] = "Rust"
languages[3] = "Python"


print(languages)
# Output: ??? 💭

######################################################################
# Answer:-
# Ans: C
# In Python, the dictionary keys are enforced with a hash table.
# When Python compares two keys 2.0 and 2 according to their hash value,
# it found them equal and overwrites the previous value.
# In short 2.0 == 2.

print(hash(3.0))    # 3
print(hash(3))      # 3
print(hash(3.0) == hash(3))  # True
# Output: {1: 'Ruby', 3.0: 'Python'}


# For more on Python follow: https://twitter.com/CodingMantras
