# Useful operations on Python list with a simple real-world case

Imagine you are creating a weather app to display the average temperature for the week in different cities.

You have a list of temperatures in Celsius for each city:

```python
WEEK_DAYS = 7
temperatures = [[30, 35, 30, 35, 30, 25, 20],
                [35, 30, 35, 30, 35, 30, 25],
                [31, 35, 40, 35, 30, 35, 31],
                [38, 43, 41, 37, 39, 34, 30]]
```

## len() function

To find the number of cities in the list, you can use the len function:

```python
num_cities = len(temperatures)
print(f"{num_cities=}")
```

## append() method

To add a new city to the list, you can use the append method:

```python
new_city = [33, 37, 37, 35, 36, 35, 30]
temperatures.append(new_city)
print(f"{temperatures=}")
```

## extend() method

To add multiple new cities to the list, you can use the extend method:

```python
cities = [[33, 37, 37, 35, 36, 35, 30],
          [32, 37, 39, 36, 36, 35, 32]]
temperatures.extend(cities)
print(f"{temperatures=}")
```

## copy() method

Copy the original list and further use the remove and pop method on the copied list. So that the original list is intact.

```python
copy_temps = temperatures.copy()
```

Note: The copy method only creates a shallow copy. So any nested objects within the list are still referenced not duplicated.

In such a case you should create a deep copy of the list if you need to modify the nested objects.

```python
from copy import deepcopy

deep_copy = deepcopy(temperatures)
```

## sum() function

To find the average temperature for each city you can use the in-built sum function:

```python
average_temps = [sum(city)//WEEK_DAYS for city in temperatures]
print(f"{average_temps=}")
```

## max() function

To find the maximum average temperature, you can use the in-built max function:

```python
max_avg_temp = max(average_temps)
print(f"{max_avg_temp=}")
```

## index() method

To find the index of the hottest city, you can use the index method of the list:

```python
index_of_hottest_city = average_temps.index(max_avg_temp)
print(f"{index_of_hottest_city=}")
```

## pop() method

Using the pop() method of the list to pop and get the weekly temps of the hottest city.

```python
weekly_temps_of_hottest_city = copy_temps.pop(index_of_hottest_city)
print(f"{weekly_temps_of_hottest_city=}")
```

## remove()

Using the remove method of the list to remove the coldest city.

```python
min_avg_temp = min(average_temps)
index_of_coldest_city = average_temps.index(min_avg_temp)
copy_temps.remove(copy_temps[index_of_coldest_city])
print(f"{index_of_coldest_city=}")
```

These are just a few examples of the operations we can perform on Python lists using built-in and list methods.

These are simple scenarios explained for learning purposes and I hope they help in enhancing your understanding of Python lists.

For more on Python follow: [@CodingMantras](https://twitter.com/CodingMantras)
