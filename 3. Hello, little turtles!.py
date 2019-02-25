'''Chapter 3'''
# Ex 1
for i in range(1000):
    print("We like Python's turtles!")

# Ex 2
'''Atributes: size, color, price
   Methods: Call, ring, close'''

# Ex 3
month = ["January", 'February', 'March', ' April', ' May',
         'June', 'July', 'August', 'September', 'October', 'December']
for i in month:
    print("One of the months of the year is " + i)

# Ex 5
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in xs:
    print(i)  # a
    print(i**2)  # b
total = 0
product = 1
for i in xs:
    total = total + i  # c
    product = product * i  # d
print("Total is", total)
print("Product is", product)

# Ex 6
wn = turtle.Screen()
broasca = turtle.Turtle()

for i in range(3): # equilateral triangle
    broasca.forward(100)
    broasca.left(120)
for i in range(4): # a square
    broasca.forward(100)
    broasca.left(90)
for i in range(6): # a hexagon
    broasca.forward(100)
    broasca.left(60)
for i in range(8): # an octagon
    broasca.forward(100)
    broasca.left(45)

# EX 7 and 8
steps = [160, -43, 270, -97, -43, 200, -940, 17, -86]
for i in steps:
    broasca.forward(100)
    broasca.left(i)
    heading = broasca.heading()
print(heading) # The turtle is heading North-West


for i in range(18):
    broasca.forward(100)
    broasca.left(20)
#20 Degrees at each corner. 360/18 = 20

# Ex 11

type(broasca)


def draw_star():
    for i in range(5):
        broasca.right(144)
        broasca.forward(100)

# draw_star()


broasca.shape("turtle")
broasca.color("blue")
broasca.stamp()
for i in range(12):
    broasca.penup()
    broasca.forward(80)
    broasca.pendown()
    broasca.forward(10)
    broasca.penup()
    broasca.forward(10)
    broasca.stamp()
    broasca.penup()
    broasca.backward(100)
    broasca.right(30)

wn.mainloop()
