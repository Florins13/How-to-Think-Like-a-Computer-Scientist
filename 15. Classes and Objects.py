# EX 1
from datetime import datetime


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reflect_x(self):  # EX 2
        a = self.x
        b = -(self.y)
        return Point(a, b)

    def slope_from_origin(self):  # Ex 3
        return (self.y-0)/(self.x-0)

    def get_line_to(self, point):  # Ex 4
        a = (point.y-self.y)//(point.x-self.x)
        b = self.y - (a*self.x)
        return (a, b)


x = Point(3, 5).reflect_x()  # Ex 2
# print(x.x, x.y)
b = Point(4, 10).slope_from_origin()  # It will fail on Point(0,0).
# print(b)
# print(Point(4, 11).get_line_to(Point(6, 15)))  # Fails when both points are 0.


Firstpoint = Point(1, 2)
Secondpoint = Point(4, 6)


def distance(point1, point2):
    dx = point2.x - point1.x
    dy = point2.y - point1.y
    dsquared = dx*dx + dy*dy
    result = dsquared**0.5
    return (result)


# print(distance(Firstpoint, Secondpoint))

# Ex 5
# The circumcircle of a Cyclic quadrilateral based on wikipedia information is:
# Parameshvara's circumradius formula
# To much geometry.... I pass.
A = Point(5, 6)
B = Point(7, 8)
C = Point(4, 5)
D = Point(3, 10)


def midpointcircle(point1, point2, point3, point4):
    d = distance(point1, point2)
    b = distance(point3, point4)
    a = distance(point1, point3)
    c = distance(point2, point3)
    print(a, b, c, d)
    s = (a + b + c + d) / 2
    R = 1/4*((((a*c+b*d)*(a*d+b*c)*(a*b+c*d))/((s-a)*(s-b)*(s-c)*(s-d)))**0.5)
    return round(R)


# print(midpointcircle(A, B, C, D))

# EX 6

class SMS_store:
    read = False

    def __init__(self):
        self.message = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        sms = (False, from_number, time_arrived, text_of_SMS)
        self.message.append(list(sms))

    def message_count(self):
        print("You have {0} messages in your inbox.".format(len(self.message)))
        return len(self.message)

    def get_unread_indexes(self):
        count = 0
        for value in self.message:
            if value[0] == False:
                count += 1
        print("You have {0} messages unreaded!".format(count))

    def get_message(self, i):
        if i not in range(len(self.message)):
            return None
        else:
            print("The message at index {0} has been set to viewed!".format(i))
            self.message[i][0] = True
            return self.message[i]

    def delete(self, i):
        del self.message[i]

    def clear(self):
        self.message = []


my_inbox = SMS_store()
my_inbox.add_new_arrival("+405152", "12:13", "Hello")
my_inbox.add_new_arrival("+405152", "13:14", "Bye")
my_inbox.add_new_arrival("+405152", "13:16", "Wait")
my_inbox.add_new_arrival("+405152", "13:18", "Or no")
my_inbox.message_count()
my_inbox.get_unread_indexes()
my_inbox.get_message(1)
my_inbox.get_message(0)
my_inbox.get_unread_indexes()
# my_inbox.delete(1)
# my_inbox.clear()
print(my_inbox.message)
