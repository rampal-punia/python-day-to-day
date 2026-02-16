"""Real-World List Operations — Weather data analysis example.

Difficulty: 🟡 Intermediate
Topics: list methods, append, extend, copy, deepcopy, index, pop, remove

Scenario: Analyze weekly temperatures for multiple cities.

Author: @rampal-punia
"""

from copy import deepcopy

WEEK_DAYS = 7


def analyze_temperatures(temperatures: list[list[int]]) -> None:
    """Perform various list operations on city temperature data.

    Args:
        temperatures: 2D list where each sublist is a city's weekly temps.
    """
    num_cities = len(temperatures)
    print(f"  Initial cities: {num_cities}")

    # append: Add one city
    new_city = [33, 37, 37, 35, 36, 35, 30]
    temperatures.append(new_city)
    print(f"  After append:   {len(temperatures)} cities")

    # extend: Add multiple cities
    more_cities = [
        [33, 37, 37, 35, 36, 35, 30],
        [32, 37, 39, 36, 36, 35, 32],
    ]
    temperatures.extend(more_cities)
    print(f"  After extend:   {len(temperatures)} cities")

    # copy vs deepcopy
    shallow = temperatures.copy()  # Inner lists are shared!
    deep = deepcopy(temperatures)  # Fully independent copy

    # Calculate averages
    averages = [sum(city) // WEEK_DAYS for city in temperatures]
    print(f"\n  Averages: {averages}")

    # Find hottest city
    max_avg = max(averages)
    hottest_idx = averages.index(max_avg)
    print(f"  Hottest city: index {hottest_idx} (avg {max_avg}°)")

    # pop: Remove and return hottest city from shallow copy
    hottest_temps = shallow.pop(hottest_idx)
    print(f"  Hottest temps:  {hottest_temps}")

    # Find coldest city
    min_avg = min(averages)
    coldest_idx = averages.index(min_avg)
    print(f"  Coldest city: index {coldest_idx} (avg {min_avg}°)")

    # Verify deepcopy is independent
    print(f"\n  Original len:   {len(temperatures)} (unchanged)")
    print(f"  Shallow len:    {len(shallow)} (lost 1 via pop)")
    print(f"  Deep copy len:  {len(deep)} (independent)")


if __name__ == "__main__":
    print("── City Temperature Analysis ──\n")
    temps = [
        [30, 35, 30, 35, 30, 25, 20],
        [35, 30, 35, 30, 35, 30, 25],
        [31, 35, 40, 35, 30, 35, 31],
        [38, 43, 41, 37, 39, 34, 30],
    ]
    analyze_temperatures(temps)

# For more on Python follow: https://x.com/rs_punia_
