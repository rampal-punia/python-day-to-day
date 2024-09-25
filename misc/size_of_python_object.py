import sys
from collections import namedtuple

languages_tuple = ("Python", "Ruby", "C++")
languages_list = ["Python", "Ruby", "C++"]
languages_dict = {'a': "Python", 'b': "Ruby", 'c': "C++"}

LangNamedTuple = namedtuple(
    'languages', ['a', 'b', 'c'])
lang_namedtuple = LangNamedTuple(**languages_dict)
print(lang_namedtuple)
print(lang_namedtuple.a)

print(sys.getsizeof(languages_tuple))   # 64
print(sys.getsizeof(languages_list))    # 80
print(sys.getsizeof(languages_dict))    # 232
print(sys.getsizeof(lang_namedtuple))   # 64
