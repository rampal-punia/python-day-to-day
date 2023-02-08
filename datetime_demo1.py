# strftime() and strptime() Format Codes

import datetime

'''
%a - Weekday as locale's abbreviated name.
%A - Weekday as locale's full name.
%w - Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
%d - Day of the month as a zero-padded decimal number.
%b - Month as locale's abbreviated name.
%B - Month as locale's full name.
%m - Month as a zero-padded decimal number.
%y - Year without century as a zero-padded decimal number.
%Y - Year with century as a decimal number.
%H - Hour (24-hour clock) as a zero-padded decimal number.
%I - Hour (12-hour clock) as a zero-padded decimal number.
%p - Locale's equivalent of either AM or PM.
%M - Minute as a zero-padded decimal number.
%S - Second as a zero-padded decimal number.
%f - Microsecond as a decimal number, zero-padded to 6 digits.
%z - UTC offset in the form ±HHMM[SS[.ffffff]] 
%Z - Time zone name
%j - Day of the year as a zero-padded decimal number.
%U - Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.
%W - Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Monday are considered to be in week 0.
%c - Locale's appropriate date and time representation.
%x - Locale's appropriate date representation.
%X - Locale's appropriate time representation
'''

day = datetime.datetime(2021, 11, 20)
print(f"{day} was a {day:%A}")

# Output: 2021-11-20 00:00:00 was a Saturday
