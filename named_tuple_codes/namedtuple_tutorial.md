# Named Tuple In Python

In Python, a namedtuple is a subclass of the built-in tuple type. It is a simple and convenient way to define a new class that behaves like an immutable tuple, but with named fields.

A namedtuple is created using the `collections.namedtuple()` function. This function takes two arguments: the name of the new class, and a list of field names.

Named tuples are like simple classes that you can create easily and quickly without writing a lot of code. You can use named tuples to store data and retrieve it later. You can also use them to create classes that cannot be changed once they are created, meaning that their values cannot be modified later on.

For example, to create a namedtuple that represents a 2D point with x and y coordinates, we could do:

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
```

This creates a new class named Point that has two fields: x and y. We can now create instances of this class using the usual tuple syntax:

```python
p = Point(1, 2)
```

We can access the fields of a namedtuple using dot notation, just like with regular objects:

```python
print(p.x)  # output: 1
print(p.y)  # output: 2
```

One advantage of using a namedtuple instead of a regular tuple is that the fields have named attributes, which makes the code more readable and less error-prone. We can also use the _asdict() method to convert a namedtuple to a dictionary:

```python
print(p._asdict())  # output: {'x': 1, 'y': 2}
```

Finally, note that namedtuple instances are immutable, which means that their fields cannot be modified once they are created. This makes them useful for representing data that should not change, such as the configuration of a program.

## Key difference between using Python dictionaries and named tuples

While both named tuples and dictionaries are useful tools for storing and accessing data in Python, there are some key differences between the two that can make named tuples a better choice for certain use cases, especially for larger datasets. Here are a few benefits of using named tuples over dictionaries:

Memory efficiency: Named tuples are implemented in C and are more memory efficient than dictionaries, which are implemented in Python. This means that for larger datasets, using named tuples can help reduce memory usage and improve performance.

Readability: Named tuples have named fields that make the code more readable and self-documenting. This can be especially useful for larger datasets with many fields, where it can be difficult to remember the keys for each field in a dictionary.

Immutable: Named tuples are immutable, which means that once a named tuple is created, its fields cannot be modified. This can be an advantage for certain use cases where immutability is important, such as caching or concurrency.

Type hints: Named tuples support type hints, which can make it easier to catch errors early in the development process and provide better documentation for the code.

Performance: Named tuples are faster than dictionaries for accessing and iterating over their values, due to their C implementation and more efficient memory layout.

Overall, while dictionaries are a powerful and flexible data structure in Python, named tuples can offer several advantages for larger datasets, especially in terms of memory efficiency, readability, immutability, type hints, and performance.

## Using namedtuple for a Point class

```python
from collections import namedtuple
import math

Point = namedtuple('Point', ['x', 'y'])

def distance_from_origin(point):
    return math.sqrt(point.x**2 + point.y**2)

def distance_between_points(point1, point2):
    dx = point1.x - point2.x
    dy = point1.y - point2.y
    return math.sqrt(dx**2 + dy**2)
```

In this example, we define a named tuple Point with two fields x and y. We also define two functions, distance_from_origin and distance_between_points, that operate on points.

The distance_from_origin function calculates the distance from a point to the origin using the Pythagorean theorem. The function takes only one argument, point, which is a named tuple representing the point.

The distance_between_points function calculates the distance between two points using the Pythagorean theorem. The function takes two arguments, point1 and point2, which are both named tuples representing points.

Using a named tuple for a point class can be a good choice if we only need to store and manipulate points with two dimensions and don't need any additional functionality beyond basic operations like calculating distances. However, if we need more functionality, a dataclass may be a better choice since it provides more flexibility for defining methods and other features.

here's an example where a named tuple may not be advisable:

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

class MutablePoint(Point):
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
```

In this example, we define a MutablePoint class that inherits from the Point named tuple. We also define a move method that modifies the x and y coordinates of the point by a given amount.

While this code may work, it is not advisable to modify the values of a named tuple because named tuples are immutable by design. In other words, once a named tuple is created, its fields cannot be modified.

Instead, it would be better to use a dataclass for the MutablePoint class, which would allow us to define mutable attributes and methods more easily:

```python
from dataclasses import dataclass

@dataclass
class MutablePoint:
    x: float
    y: float

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
```

In this example, we define a MutablePoint dataclass with mutable attributes x and y, and a move method that modifies the coordinates by a given amount. Since a dataclass is mutable by default, it is a better choice for this use case than a named tuple.

Great to hear that! Here are some additional examples that can help you understand the differences and benefits of named tuples and dataclasses:

Representing complex data structures: Both named tuples and dataclasses can be used to represent complex data structures. For example, you can use a named tuple to represent a 2D point or a dataclass to represent a book. However, if you need more functionality or flexibility, such as methods for transforming or manipulating the data, a dataclass may be a better choice.

API responses: Named tuples can be a good choice for representing data returned by an API. For example, you can use a named tuple to represent a response from a weather API with fields like temperature, humidity, and pressure. Named tuples are lightweight, immutable, and can be easily serialized to JSON.

Configuration settings: Dataclasses can be a good choice for representing configuration settings for an application. For example, you can use a dataclass to represent settings like database_url, debug_mode, and log_level. Dataclasses provide a convenient way to define default values and other metadata for each setting.

Database records: Dataclasses can also be a good choice for representing database records. For example, you can use a dataclass to represent a row in a database table with fields like id, name, and email. Dataclasses provide a convenient way to define the attributes of each record and also allow you to define methods for manipulating the data.

API input validation: Dataclasses can also be used for input validation in API endpoints. For example, you can use a dataclass to represent the data sent in a POST request with fields like username, email, and password. Dataclasses provide a convenient way to define the expected fields and types of the input data, and also allow you to define validation methods.

I hope these examples help you understand the benefits and use cases of named tuples and dataclasses.

an example of using named tuples for a weather data class:

```python
from collections import namedtuple


WeatherData = namedtuple('WeatherData', ['date', 'temperature', 'humidity'])


class WeatherReport:
    def __init__(self):
        self.weather_data = []

    def add_weather_data(self, date, temperature, humidity):
        data = WeatherData(date, temperature, humidity)
        self.weather_data.append(data)

    def get_average_temperature(self):
        temperatures = [data.temperature for data in self.weather_data]
        return sum(temperatures) / len(temperatures)

    def get_average_humidity(self):
        humidities = [data.humidity for data in self.weather_data]
        return sum(humidities) / len(humidities)


wr = WeatherReport()
wr.add_weather_data('26 Mar', 37, 65)
wr.add_weather_data('27 Mar', 36, 62)
wr.add_weather_data('28 Mar', 38, 72)

print(wr.weather_data)
print(wr.get_average_temperature())
print(wr.get_average_humidity())
```

In this example, we define a named tuple WeatherData with three fields: date, temperature, and humidity. We then define a class WeatherReport that stores a list of WeatherData instances.

The add_weather_data method is used to add new weather data to the report. The method creates a new instance of WeatherData using the namedtuple constructor and appends it to the weather_data list.

The get_average_temperature and get_average_humidity methods calculate the average temperature and humidity, respectively, of all the weather data in the report. They use list comprehension to extract the temperature and humidity values from the WeatherData instances and then calculate the average using the built-in sum and len functions.

Using a named tuple in this example makes the code more readable and self-documenting, since each WeatherData instance has named fields that are easily accessible using dot notation. Additionally, named tuples are memory-efficient and immutable, which can be beneficial for larger datasets.
