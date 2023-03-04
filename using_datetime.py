'''✨ Python: Using datetime module ✨

The datetime module is a built-in module to work with 
dates and times in Python. This module provides classes like 
datetime, date, time, timedelta, etc.
'''

from datetime import datetime

# today: year-month-date, hr:min:sec.millisec,
today = datetime.today()
print(today)

# date part of today
date = today.date()
print(date)

# Month part of today
month = today.month
print(month)

# Day part of today
day = today.day
print(day)

# You can try: today.hour, today.minute, weekday = today.weekday()

# A simple example for comparison of dates


# Get today's date
today = datetime.today()

# Create a date object for a specific date
specific_date = datetime(2023, 4, 15)

# Compare the two dates
if today < specific_date:
    print("The specific date is in the future.")
elif today == specific_date:
    print("Today is the specific date!")
else:
    print("The specific date has already passed.")
