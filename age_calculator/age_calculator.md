# Create a basic Age Calculator

Calculate the age of the user if the year month and day of birth are given.

```python
'''✨ Age Calculator In Python.✨'''
from datetime import date

# 👉 Given Date of Birth (Year, month, date)
year_of_birth = 1995
month_of_birth = 1
day_of_birth = 1

today = date.today()
print(f"Today: {today}")

# 👉 Print DOB
dob = date(year_of_birth, month_of_birth, day_of_birth)
print(f"DOB: {dob}")

# 👉 Days till today
total_days = (today-dob).days
print(f"Days: {total_days}")

# 👉 Years till today
years = total_days/365
print(f"In Years: {years:.2f}")

# Note: This does not take into account the leap year.
```

```bash
Output:

Today: 2023-01-26
DOB: 1995-01-01
Days: 10252
In Years: 28.09
```

As you would have noticed that this method is not 100% accurate as it does not take into account leap years.

If you want to get a more accurate result you can use the dateutil library.

For example:

```python
'''🚀 Age Calculator In Python'''
from datetime import date
import dateutil.relativedelta as rd

# 👉 Given Date of Birth (Year, month, date)
year_of_birth = 1995
month_of_birth = 1
day_of_birth = 1

today = date.today()
print(f"Today: {today}")

# 👉 Print DOB
dob = date(year_of_birth, month_of_birth, day_of_birth)
print(f"DOB: {dob}")

# 👉 Take into account leap years and the difference in months and days also.
diff = rd.relativedelta(today, dob)
print(f"Age: {diff.years} years, {diff.months} months, {diff.days} days")
```

```output
Output:

Today: 2023-01-26
DOB: 1995-01-01
Age: 28 years, 0 months, 25 days
```
