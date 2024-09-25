# Using Namedtuple and Dataclasses to Create a Weather Report in Python

```python
from dataclasses import dataclass
from collections import namedtuple
from typing import List

WeatherData = namedtuple('WeatherData', ['date', 'temperature', 'humidity'])


@dataclass
class WeatherReport:
    weather_data: List[WeatherData]

    def add_weather_data(self, data: WeatherData):
        self.weather_data.append(data)

    def get_average_temperature(self):
        temperatures = [data.temperature for data in self.weather_data]
        return sum(temperatures) / len(temperatures)

    def get_average_humidity(self):
        humidities = [data.humidity for data in self.weather_data]
        return sum(humidities) / len(humidities)


wr = WeatherReport([])
wr.add_weather_data(WeatherData('26 Mar', 37, 65))
wr.add_weather_data(WeatherData('27 Mar', 36, 62))
wr.add_weather_data(WeatherData('28 Mar', 38, 72))

print(wr.weather_data)
print(wr.get_average_temperature())
print(wr.get_average_humidity())
```

The code above demonstrates the use of both namedtuple and dataclass to create a WeatherReport class that contains a list of weather data consisting of dates, temperatures, and humidity.

The namedtuple is used to define the structure of the WeatherData class with three fields: date, temperature, and humidity. namedtuple provides a way to create simple, lightweight classes with named fields that can be used to represent immutable data.

The dataclass decorator is used to create the WeatherReport class. The WeatherReport class has a single field weather_data that contains a list of WeatherData objects.

By using namedtuple and dataclass together, we can create classes with immutable attributes and simple class structures. These classes are easier to read, write and maintain than regular Python classes.

The add_weather_data method allows the addition of new WeatherData objects to the WeatherReport object's weather_data list.

The get_average_temperature and get_average_humidity methods calculate the average temperature and humidity of the weather data stored in the WeatherReport object's weather_data list.

Overall, the use of namedtuple and dataclass in this code provides a concise, readable and efficient way to define and use these classes. It also helps reduce the amount of code needed to define these classes and their methods.
