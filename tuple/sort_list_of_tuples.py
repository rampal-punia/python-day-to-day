'''✨ Sorting a list of tuples on the basis of the second element. ✨'''

# Method 1: Using sorted Function
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sorted_list = sorted(sample_list, key=lambda x: x[1])
print(sorted_list)

# Method 2: Using sort method of list
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sample_list.sort(key=lambda x: x[1])
print(sample_list)


# Method 3: Using Custom Function
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def sort_by_second_element(x):
    return x[1]


sorted_list = sorted(sample_list, key=sort_by_second_element)
print(sorted_list)

# Method 4: Using List Comprehension
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = [x for _, x in sorted([(y[1], y) for y in sample_list])]
print(sorted_list)


# Method 5: Using A While Loop (Project specific)
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
i = 1

while i < len(sample_list):
    j = i
    while j > 0 and sample_list[j-1][1] > sample_list[j][1]:
        sample_list[j], sample_list[j-1] = sample_list[j-1], sample_list[j]
        j -= 1
    i += 1

print(sample_list)
