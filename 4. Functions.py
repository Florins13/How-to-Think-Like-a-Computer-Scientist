# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      florins
#
# Created:     03/12/2018
# Copyright:   (c) florins 2018
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
florin = turtle.Turtle()
florin.shape("turtle")
florin.color("blue")
florin.pensize(3)
florin.speed(5)

'''
for i in range(4):
    for i in range(4):
        florin.forward(20)
        florin.left(90)
    florin.penup()
    florin.forward(40)
    florin.pendown()
'''

# EX 2
'''
size = 20
for i in range(5):
    for i in range(4):
        florin.forward(size)
        florin.left(90)
    florin.right(135)
    florin.penup()
    florin.forward(15)
    florin.left(135)
    florin.pendown()
    size += 20
'''


# Ex 3
def draw_poly(broasca, n, sz):
    for i in range(n):
        broasca.forward(sz)
        broasca.left(360/n)


#draw_poly(florin, 8, 50)

# Ex 4
'''
def square(broasca):
    for i in range(4):
        broasca.forward(100)
        broasca.left(90)

for i in range(20):
    square(florin)
    florin.right(20)
'''

# Ex 5

'''
def draw_patrat(broasca, latura):
    broasca.left(91) # If you change here the angle to 90 you will get the first draw.
    broasca.forward(latura)

size = 2

for i in range(100):
    size = size + 3
    draw_patrat(florin, size)
'''

# Ex 6


def draw_equitriangle(t, sz):
    draw_poly(t, 3, sz)

#draw_equitriangle(florin, 100)

# Ex 7


def sum_to(n):
    sum = 0
    for i in range(n+1):
        sum = sum + i
        print(sum)
# sum_to(10)

# Ex 8


def area_of_circle(r):
    area = 3.14159 * r**2
    print(area)
    return area


# Ex 9
def draw_star():
    for i in range(5):
        florin.right(144)
        florin.forward(100)


# Ex 10
for i in range(5):
    draw_star()
    # florin.right(144)
    # florin.penup()
    florin.right(144)
    florin.forward(400)
    florin.pendown()

wn.mainloop()
