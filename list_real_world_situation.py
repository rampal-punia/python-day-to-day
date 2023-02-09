'''✨ Useful operations on Python lists with a simple real-world case. ✨'''
from copy import deepcopy

WEEK_DAYS = 7
temperatures = [[30, 35, 30, 35, 30, 25, 20],
                [35, 30, 35, 30, 35, 30, 25],
                [31, 35, 40, 35, 30, 35, 31],
                [38, 43, 41, 37, 39, 34, 30]]


num_cities = len(temperatures)
print(f"{num_cities=}")

new_city = [33, 37, 37, 35, 36, 35, 30]
temperatures.append(new_city)
print(f"{temperatures=}")

cities = [[33, 37, 37, 35, 36, 35, 30],
          [32, 37, 39, 36, 36, 35, 32]]
temperatures.extend(cities)
print(f"{temperatures=}")

copy_temps = temperatures.copy()
deep_copy = deepcopy(temperatures)

average_temps = [sum(city)//WEEK_DAYS for city in temperatures]
print(f"{average_temps=}")

max_avg_temp = max(average_temps)
print(f"{max_avg_temp=}")


index_of_hottest_city = average_temps.index(max_avg_temp)
print(f"{index_of_hottest_city=}")

weekly_temps_of_hottest_city = copy_temps.pop(index_of_hottest_city)
print(f"{weekly_temps_of_hottest_city=}")

min_avg_temp = min(average_temps)
index_of_coldest_city = average_temps.index(min_avg_temp)
copy_temps.remove(copy_temps[index_of_coldest_city])
print(f"{index_of_coldest_city=}")
print(f"{copy_temps=}")
print(f"{temperatures=}")
print(deep_copy)


# For more on Python follow: https://twitter.com/CodingMantras
