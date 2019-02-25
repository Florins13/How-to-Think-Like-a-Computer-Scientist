import turtle           # Tess becomes a traffic light.
#EX 1

import turtle

turtle.setup(400, 500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle

size = 0
# The next four functions are our "event handlers".


def h1():
    tess.forward(30)


def h2():
    tess.left(45)


def h3():
    tess.right(45)


def h4():
    wn.bye()                    # Close down the turtle window


def h5():
    tess.color("Green")


def h6():
    tess.color("Red")


def h7():
    tess.color("Blue")


def h8():
    global size
    if size <= 20 and size > 0:
        size = size - 1
    else:
        wn.title("You cant go bellow 0!")
        size = 0
    tess.pensize(size)
    wn.title("Current size: {0}".format(size))


def h9():
    global size
    if size < 20 and size >= 0:
        size = size + 1
    else:
        size = 20
        wn.title("You cant go higher then 20!")
    tess.pensize(size)
    wn.title("Current size: {0}".format(size))


def h10():
    circle = 30
    tess.circle(circle)


def h11():
    tess.reset()


def h12():
    tess.stamp()


# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(h5, "g")
wn.onkey(h6, "r")
wn.onkey(h7, "b")
wn.onkey(h8, "m")
wn.onkey(h9, "p")
wn.onkey(h10, "x")
wn.onkey(h11, "c")
wn.onkey(h12, "a")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()


'''EX 2,3,4 and 5'''

turtle.setup(700, 800)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
alex = turtle.Turtle()

verde = turtle.Turtle()
portocaliu = turtle.Turtle()
rosu = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


def draw_housing2():
    """ Draw a nice housing to hold the traffic lights """
    alex.penup()
    alex.forward(200)
    alex.pendown()
    alex.pensize(3)
    alex.color("black", "darkgrey")
    alex.begin_fill()
    alex.forward(80)
    alex.left(90)
    alex.forward(200)
    alex.circle(40, 180)
    alex.forward(200)
    alex.left(90)
    alex.end_fill()


draw_housing()
draw_housing2()


def tesslight():
    tess.penup()
    # Position tess onto the place where the green light should be
    tess.forward(40)
    tess.left(90)
    tess.forward(50)
    # Turn tess into a big green circle
    tess.shape("circle")
    tess.shapesize(3)
    tess.fillcolor("green")


tesslight()


def verdebec():
    verde.penup()
    verde.forward(200)
    verde.pendown()
    verde.penup()
    # Position tess onto the place where the green light should be
    verde.forward(40)
    verde.left(90)
    verde.forward(50)
    # Turn tess into a big green circle
    verde.shape("circle")
    verde.shapesize(3)
    verde.fillcolor("green")


verdebec()


def rosubec():
    rosu.penup()
    rosu.forward(200)
    rosu.pendown()
    rosu.penup()
    # Position tess onto the place where the green light should be
    rosu.forward(40)
    rosu.left(90)
    rosu.forward(190)
    # Turn tess into a big green circle
    rosu.shape("circle")
    rosu.shapesize(3)
    rosu.fillcolor("red")


rosubec()


def portocaliubec():
    portocaliu.penup()
    portocaliu.forward(200)
    portocaliu.pendown()
    portocaliu.penup()
    # Position tess onto the place where the green light should be
    portocaliu.forward(40)
    portocaliu.left(90)
    portocaliu.forward(120)
    # Turn tess into a big green circle
    portocaliu.shape("circle")
    portocaliu.shapesize(3)
    portocaliu.fillcolor("orange")


portocaliubec()
# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    wn.ontimer(advance_state_machine, 1000)  # EX2
    if state_num == 0:       # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:     # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:                    # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0


def green_state():
    global state_num
    if state_num == 0:
        portocaliu.fillcolor("lightgreen")
        rosu.fillcolor("lightgreen")
        verde.fillcolor("green")
        state_num = 1


def orange_green_state():
    global state_num
    if state_num == 1:
        portocaliu.fillcolor("orange")
        rosu.fillcolor("lightgreen")
        verde.fillcolor("green")
        state_num = 2


def orange_state():
    global state_num
    if state_num == 2:       # Transition from state 0 to state 1
        rosu.fillcolor("lightgreen")
        verde.fillcolor("lightgreen")
        portocaliu.fillcolor("orange")
        state_num = 3


def red_state():
    global state_num
    if state_num == 3:
        portocaliu.fillcolor("lightgreen")
        verde.fillcolor("lightgreen")
        rosu.fillcolor("red")
        state_num = 0


def lol():
    wn.ontimer(green_state, 1000)
    wn.ontimer(orange_green_state, 4000)
    wn.ontimer(orange_state, 5000)
    wn.ontimer(red_state, 6000)
    wn.ontimer(lol, 7000)


'''
def start():
    green_state()
    orange_green_state()
    orange_state()
    red_state()
'''

# Bind the event handler to the space key.
# EX2
wn.onkey(advance_state_machine, "space")
wn.onkey(lol, "x")
wn.listen()                      # Listen for events
wn.mainloop()
