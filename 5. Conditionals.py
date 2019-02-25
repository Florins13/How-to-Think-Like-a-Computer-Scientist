# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      florins
#
# Created:     08/12/2018
# Copyright:   (c) florins 2018
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import turtle
dayss = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def days(x, zile):
    if x == '1':
        print(zile[0])
    elif '2' == x:
        print(zile[1])
    elif '3' == x:
        print(zile[2])
    elif '4' == x:
        print(zile[3])
    elif '5' == x:
        print(zile[4])
    elif '6' == x:
        print(zile[5])
    else:
        print(zile[6])


def days_in_vacation():
    startstr = input("Starting day number")
    start = int(startstr)
    lengthstr = input("How much will you stay?")
    length = int(lengthstr)
    dayofreturn = ((start + length) % 7) % 7
    dayofreturnstr = str(dayofreturn)
    print(dayofreturnstr)
    return days(dayofreturnstr, dayss)


# days_in_vacation()

def function(mark):
    if mark >= 75:
        return "First"
    if mark >= 70 and mark < 75:
        return "Upper Second"
    if mark >= 60 and mark < 70:
        return "Second"
    if mark >= 50 and mark < 60:
        return "Third"
    if mark >= 45 and mark < 50:
        return "F1 Supp"
    if mark >= 40 and mark < 45:
        return "F2"
    if mark < 40:
        return "F3"


# Ex 7,8,9


def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    if height >= 200:
        t.color("blue", "red")
    if height >= 100 and height < 200:
        t.color("blue", "yellow")
    if height < 100:
        t.color("blue", "green")
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("  " + str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
    t.forward(10)


wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color("blue", "red")
tess.pensize(3)

xs = [-200, 48, 117, 200, 240, 160, 260, 220, -50]

for a in xs:
    draw_bar(tess, a)

# Ex 10


def find_hypot(latura1, latura2):
    x = latura1**2 + latura2**2
    y = x**0.5
    print(y)


# Ex 11

def is_rightangled(small, small2, longest):
    x = small**2 + small2**2
    y = longest**2
    if abs(y-x) < 0.000001:
        return True
    else:
        return False


#print(is_rightangled(5, 12, 13))


# Ex 12


def is_rightangled(latura, latura1, latura2):
    if latura > latura1 or latura2:
        x = latura**2
        y = latura1**2 + latura2**2
        if abs(x-y) < 0.000001:
            return True
        else:
            return False
    elif latura1 > latura or latura2:
        x = latura1**2
        y = latura**2 + latura2**2
        if abs(x-y) < 0.000001:
            return True
        else:
            return False
    else:
        x = latura2**2
        y = latura**2 + latura1**2
        if abs(x-y) < 0.000001:
            return True
        else:
            return False
