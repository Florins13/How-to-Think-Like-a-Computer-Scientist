from unit_tester import test
import calendar
import math
from copy import deepcopy
'''
cal = calendar.TextCalendar()
cal.pryear(2012)  # return a full calendar of the 2012 year
# EX 1b
cal.setfirstweekday(calendar.THURSDAY)  # sets the starting they of the week
# EX 1c
print(cal.formatmonth(2018, 9))  # print the month of your second argument
cal.prmonth(2018, 9)  # return the month of your second argument

# EX 1d
# fist argument->starting day, second -> the language of the days
d = calendar.LocaleTextCalendar(7, "american")
d.pryear(2012)  # print a calendar of the 2012 year
# EX 1e
print(calendar.isleap(2022))
# calendar.isleap expects as arguments year(integers), it returns a boolean value, is a boolean function
'''
# Ex 2a -> many :D
# Ex 2b -> Return the ceiling of x, the smallest integer greater than or equal to x.
# -> Return the floor of x, the largest integer less than or equal to x.
# print(math.floor(-22.93232))
# print(math.ceil(-22.03232))
# Ex 2c -> by making a function that returns its argument at the power of 0.5
# Ex 2d -> math.pi (The mathematical constant π = 3.141592…, to available precision.)
# -> math.e (The mathematical constant e = 2.718281…, to available precision.)

# Ex 3. -> This module provides the method "copy", which allows a complete copy of a arbitrary list, i.e. shallow and other lists.
# -> This exercise would come in handy for the last exercise, where we would swap two lists.
string = ["florin", "echipa"]
b = deepcopy(string)
b[1] = ['gege']

#print(string, b)

# Ex 4

#mymodule1, mymodule2, namespace_test.py

# Ex 6
'''
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

# Ex 7
s = "If we took the bones out, it wouldn't be crunchy, would it?"


def myreplace(old, new, s):
    a = new.join(s.split(old))
    print(a)
    return a


test(myreplace(",", ";", "this, that, and some other thing") ==
     "this; that; and some other thing")
test(myreplace(" ", "**",
               "Words will now be separated by stars.") == "Words**will**now**be**separated**by**stars.")
