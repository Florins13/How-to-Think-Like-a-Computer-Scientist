from unit_tester import test


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return 2*(self.width + self.height)

    def flip(self):
        oldwidth = self.width
        oldheight = self.height
        self.width = oldheight
        self.height = oldwidth
        return self.width, self.height

    def contains(self, point):
        width = point.x
        height = point.y
        if width >= 10 or height >= 5:
            return False
        elif width < 0 or height < 0:
            return False
        else:
            return True


'''
box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)    # In my video game
print("box: ", box)
print("bomb: ", bomb)
r = Rectangle(Point(0, 0), 10, 5)
test(r.area() == 50)
r = Rectangle(Point(0, 0), 10, 5)
test(r.perimeter() == 30)
r = Rectangle(Point(100, 50), 10, 5)
test(r.width == 10 and r.height == 5)
r.flip()
test(r.width == 5 and r.height == 10)
r = Rectangle(Point(0, 0), 10, 5)
test(r.contains(Point(0, 0)))
test(r.contains(Point(3, 3)))
test(not r.contains(Point(3, 7)))
test(not r.contains(Point(3, 5)))
test(r.contains(Point(3, 4.99999)))
test(not r.contains(Point(-3, -3)))
r1 = Rectangle(Point(1, 1), 10, 5)
'''

# -----> test down


def checkcolision(rectangle1, rectangle2):
    x = rectangle1.corner.x
    y = rectangle1.corner.y
    height_rectangle_1 = rectangle1.height - y
    width_rectangle_1 = rectangle1.width - x
    x1 = rectangle2.corner.x
    y1 = rectangle2.corner.y
    height_rectangle_2 = rectangle2.height - y1
    width_rectangle_2 = rectangle2.width - x1


checkcolision(r, r1)
