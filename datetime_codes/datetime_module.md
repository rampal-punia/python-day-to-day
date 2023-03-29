# Datetime Module Of Python

The datetime module is a built-in module in Python that allows us to work with dates and times. It has several built-in classes, such as date, time, datetime, timedelta, etc., that allow for easy manipulation of date and time values in Python.

## Importing `datetime` module

```python
# datetime module import
import datetime

# Importing the datetime class from datetime module.
from datetime import datetime
```

## Creating a datetime object

```python
# Importing the datetime class from datetime module.
from datetime import datetime

# Creating a datetime object for the current date and time
now = datetime.now()
print("Current date and time: ", now)
```

This will create a datetime object for the current date and time, and display it to the console.

## Working with datetime attributes

Work with different attributes of the datetime object, such as the year, month, day, hour, minute, and second.

Here's an example code:

```python
from datetime import datetime

now = datetime.now()
# Accessing different attributes of the datetime object
print("Year: ", now.year)
print("Month: ", now.month)
print("Day: ", now.day)
print("Hour: ", now.hour)
print("Minute: ", now.minute)
print("Second: ", now.second)
print("MicroSecond: ", now.microsecond)

# For week number info
year, week_num, weekday = now.isocalendar()
print(week_num)
```

This code will display the different attributes of the datetime object to the console.

## Formatting datetime objects

Datetime objects can be formatted in different ways using the `strftime` method. Here's an example code:

```python
# Formatting datetime objects
print("Date and time in ISO format: ", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Date and time in a different format: ", now.strftime("%d/%m/%Y %H:%M:%S"))
```

## Creating a date object

```python
from datetime import date
# Creating a date object
today = date.today()
print("Today's date: ", today)
```

## Working with date attributes

```python
from datetime import date
today = date.today()
# Accessing different attributes of the date object
print("Year: ", today.year)
print("Month: ", today.month)
print("Day: ", today.day)
```

## Creating a time object

```python
from datetime import time
# Creating a time object
t = time(12, 30, 45)
print("Time: ", t)
```

## Working with time attributes

```python
import datetime
t = datetime.time(10, 30, 45)

# Accessing different attributes of the time object
print("Hour: ", t.hour)
print("Minute: ", t.minute)
print("Second: ", t.second)
print("Microsecond: ", t.microsecond)
print("Timezone: ", t.tzinfo)
```

Note: The tzinfo attribute will return None in this example because we did not specify a timezone when creating the time object. To set the timezone, you can use the pytz module or the timezone class from the datetime module.

The datetime module provides a range of formatting options to convert datetime objects into different string formats. Additionally, you can use the module to perform various time zone calculations and conversions.
