import turtle


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

wn.mainloop()


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

def area_of_circle(r):
    area = 3.14159 * r ** 2
    return area


response = float(input("Care este raza cercului?"))
valoare = area_of_circle(response)
print(valoare)


# -------------------------------------------------------------------------------
# Name:        1 star 5 star
# Purpose:
#
# Author:      florins
#
# Created:     26/11/2018
# Copyright:   (c) florins 2018
# Licence:     <your licence>
# -------------------------------------------------------------------------------

wn = turtle.Screen()
florin = turtle.Turtle()


def draw_star():
    for i in range(5):
        florin.right(144)
        florin.forward(100)


for i in range(5):
    draw_star()
    # florin.right(144)
    # florin.penup()
    florin.right(144)
    florin.forward(400)
    florin.pendown()

florin.speed(10)
wn.mainloop()
