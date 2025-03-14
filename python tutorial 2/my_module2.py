# import my_module as mm
# or
from my_module import find_index, test
import sys

import datetime
import calendar

courses = ['history', 'math', 'physics', 'compSci']

# print(mm.find_index(courses, 'math'.lower()))
# print(find_index(courses, 'math'.lower()))


# print(sys.path)

calen = calendar.TextCalendar()

print(calen.formatyear(2025))