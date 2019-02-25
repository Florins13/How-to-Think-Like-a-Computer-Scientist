# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      florins
#
# Created:     24/12/2018
# Copyright:   (c) florins 2018
# Licence:     <your licence>
# -------------------------------------------------------------------------------


import sys
import math


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def turn_clockwise(p):
    if p == 'N':
        return 'S'
    elif p == 'S':
        return 'N'
    elif p == 'W':
        return 'E'
    elif p == 'E':
        return 'W'
    else:
        return None


def day_name(a):
    # print(a)
    dayss = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for e in dayss:
        if a == 0:
            return (dayss[6])
        elif a == 1:
            return dayss[0]
        elif a == 2:
            return dayss[1]
        elif a == 3:
            return dayss[2]
        elif a == 4:
            return dayss[3]
        elif a == 5:
            return dayss[4]
        elif a == 6:
            return dayss[5]
        return None


def day_num(day):
    dayss = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for e in dayss:
        if day in dayss:
            return (dayss.index(day))
        return None


def day_add(daystart, number):
    day_start = day_num(daystart)
    # print(day_start)
    # day_return_final = ((day_start + number) % 7) % 7
    day_return_final = day_start + number
    # print(day_return_final)
    day_return_final_modulo_1 = day_return_final % 7
    # print(day_return_final_modulo_1)
    day_return_final_modulo_2 = day_return_final_modulo_1 % 7
    # print(day_return_final_modulo_2)
    return day_name(day_return_final_modulo_2)


def days_in_month(luni):
    months = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
              'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
    for e in months:
        if luni in months:
            return months[luni]


def to_secs(h, m, s):
    hourstosec = h * 60
    minutestosec = (hourstosec + m) * 60 + s
    return int(minutestosec)


def hours_in(sec):
    minutes = sec / 60
    hours = minutes / 60
    return int(hours)


def minutes_in(sec):
    minutes = (sec / 60) % 60
    print(150 % 60)
    return int(minutes)


def seconds_in(sec):
    seconds = (sec % 60)
    print(seconds)
    return int(seconds)


def compare(a, b):
    if a > b:
        return 1
    if a == b:
        return 0
    if a < b:
        return -1


def hypotenuse(a, b):
    c = a**2 + b**2
    return math.sqrt(c)


def slope(x1, y1, x2, y2):
    y = float(y2-y1)
    x = float(x2-x1)
    yx = float(y/x)
    return yx


def intercept(x1, y1, x2, y2):
    y = y2-(slope(x1, y1, x2, y2)*x2)
    return y


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def is_odd(n):
    if n % 2 != 0:
        return False
        print("Numarul este impar!")
    is_even(n)


def is_factor(f, n):
    if n % f == 0:
        #print("Is multiple")
        return True
    if n % f != 0:
        #print("Is not multiple")
        return False


def is_multiple(f, n):
    if f % n == 0:
        #print("Is multiple")
        return True
    if f % n != 0:
        #print("Is not multiple")
        return False


def f2c(t):
    celsius = round((t - 32) * 5/9)
    return celsius


def c2f(t):
    fahrenheit = round((t * 9/5) + 32)
    return fahrenheit


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)


test_suite()
