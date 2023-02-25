'''✨ Check if a string is Palindrome ✨

A palindrome is a word, number, phrase, or another sequence of 
characters which read the same backward as forward, such as "Tenet".
'''

# Method 1:


def is_palindrome(string):
    if string.lower() == string[::-1].lower():
        return True
    else:
        return False


# Method 2:
def is_palindrome(string):
    return string.lower() == string[::-1].lower()


print(is_palindrome("click"))
print(is_palindrome("Rotator"))


# For more on Python follow: https://twitter.com/CodingMantras
