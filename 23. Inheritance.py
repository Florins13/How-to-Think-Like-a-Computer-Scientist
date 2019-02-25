import random
import turtle

# Ex 2 & 3


class TurtleGTX(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.myWn = turtle.Screen()
        self.color("green")
        self.speed(1)
        self.odometer = 0
        self.breaktire = random.randrange(0, 500)
        print(self.breaktire)

    def main(self):
        turtle.mainloop()

    def forward(self, x):
        for i in range(abs(x)):
            self.odometer += 1
            try:
                if self.odometer > self.breaktire:
                    breaktire_error = ValueError("Your tire broke.")
                    raise breaktire_error
            except:
                self.change_tire()  # comment this and you wont get far away!
                if self.odometer > self.breaktire:
                    raise breaktire_error

        self.fd(x)
        self.__str__()

    def change_tire(self):
        self.breaktire = 2000  # we are putting a new tire

    def __str__(self):
        print("Odometer is: " + str(self.odometer))


my_turtle = TurtleGTX()

my_turtle.forward(50)
for i in range(10):
    my_turtle.forward(50)
    my_turtle.right(45)
my_turtle.forward(-100)

my_turtle.__str__()
my_turtle.main()
