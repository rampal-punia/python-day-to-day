def func(x):
    return x * 3


new_func = func


def func(x):
    return x+2


my_func = func

print(new_func(2))
print(my_func(2))
