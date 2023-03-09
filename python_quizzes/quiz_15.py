def add_number(a, b):
    return a + b


def add_number(a, b):
    return a + b


func1 = add_number(4, 5)
func2 = add_number(4, 5)


print(func1 is func2)

my_strange_set = {func1, func2}
print(len(my_strange_set))
