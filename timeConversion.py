#!/bin/python3
import sys

print("Enter a time: ")
print("(hh:mm:ss AM or PM)")

time = input().strip()
(hours, minutes, rest_of_hour) = time.split(':')

minutes = int(minutes)
hours = int(hours)

if rest_of_hour.find('PM') != -1:
    timeFormat = "PM"
    if hours >= 1 and hours <= 11:
        hours += 12
else:
    timeFormat = "AM"
    if hours == 12:
        hours = 0
        
rest_of_hour = rest_of_hour.replace(timeFormat, '')
hours = '{:02}'.format(hours)
minutes = '{:02}'.format(minutes)

result = str(hours) + ":" + str(minutes) + ":" + rest_of_hour
print(result)
