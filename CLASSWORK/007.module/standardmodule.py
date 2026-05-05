import math 

print(math.pi)
print(math.e)
print(math.sqrt(25))
print(math.sin(90))


import os

os.mkdir("NEW FOLDER")
os.rmdir("NEW FOLDER")
print

import sys
print(sys.version)

import datetime

date = datetime.datetime.now()
print(date.day)
print(date.year)
print(date.month)
print(date.time())


import calendar

print(calendar.month(2026,12))
print(calendar.calendar(2026))


import random
n = random.randint(100,999)
print(n)