import sys
import turtle


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


'''EX1'''
# print(list(range(10, 0, -2)))
# print(list(range(0, 10, 2)))
# First rule: If start > stop, we get an descending sequence of numbers with the
# third parameter 'step' setting the pattern of numbers.
# EX: print(list(range(10, 0, -2))) --->    [10, 8, 6, 4, 2]
# EX: print(list(range(0, 10)))     --->    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Second rule : If start < stop, we get an ascending sequence of numbers again
# with the third parameter 'step' setting the pattern of numbers.
# EX: print(list(range(0, 10, 2)))  --->    [0, 2, 4, 6, 8]

'''EX2
wn = turtle.Screen()
tess = turtle.Turtle()
tess.color("blue")
alex = tess
alex.color("hotpink")
print(alex == tess)
wn.listen()
wn.mainloop()
Since strings are immutable, Python optimizes resources by making two names that refer to the same string value refer to the same object.
Since variables refer to objects, if we assign one variable to another, both variables refer to the same object.
Starting from this definitions we already know that alex and tess are refering
the same object, namely turtle.Turtle(). That means of we change the color of
alex we change the color of the object is refering to so implicitely tess will
have the color of the object is refering to. :)'''

'''EX3
a = [1, 2, 3]
b = a[:]
b[0] = 5
# print(a, b, (a is b))   ----> [1, 2, 3] [5, 2, 3] False
# Ok, so a is refering to one object [1,2,3] and b is refering to another object
# because using a[:] we clone that list of a by using slice operator.
'''

'''EX4
this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
that = this
print("Test 2: {0}".format(this is that))
# At the begining each list is refering to another object output will be False, but when we assign
# that to this (that = this), 'that' will refer to the object 'this' is refering
# too, output will be True.
'''

'''EX5'''


def add_vectors(u, v):
    list = []
    for i in range(len(u)):
        new_elem = u[i] + v[i]
        list.append(new_elem)
        print(list)
    return list


# test(add_vectors([1, 1], [1, 1]) == [2, 2])
# test(add_vectors([1, 2], [1, 4]) == [2, 6])
# test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
'''EX6'''


def scalar_mult(s, v):
    list = []
    for i in range(len(v)):
        new_elem = s * v[i]
        list.append(new_elem)
    return list


# test(scalar_mult(5, [1, 2]) == [5, 10])
# test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
# test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
'''EX7'''


def dot_product(u, v):
    list = []
    b = 0
    for i in range(len(u)):
        new_elem = u[i]*v[i]
        list.append(new_elem)
    for i in range(len(list)):
        b = b + list[i]
    return b


# test(dot_product([1, 1], [1, 1]) == 2)
# test(dot_product([1, 2], [1, 4]) == 9)
# test(dot_product([1, 2, 1], [1, 4, 3]) == 12)

'''EX8'''


def cross_product(u, v):
    a = 0
    b = 0
    list = []
    first_v = u[1]*v[2] - u[2]*v[1]
    second_v = u[2]*v[0] - u[0]*v[2]
    third_v = u[0]*v[1] - u[1]*v[0]
    list.append(first_v)
    list.append(second_v)
    list.append(third_v)
    return list


# test(cross_product([1, -7, 1], [5, 2, 4]) == [-30, 1, 37])
# test(cross_product([7, 3, -4], [1, 0, 6]) == [18, -46, -3])

'''EX9'''
song = "The rain in Spain..."
# print(song.split())
# print(" ".join(song.split()))
# print(song)
# Ok so song.split() does this: ['The', 'rain', 'in', 'Spain...']
# print(";".join(song.split())) does this: The;rain;in;Spain...
# print(" ".join(song.split())) does this: The rain in Spain...
# Song with dated function are actually the same thing, our function just splits
# the characters into a list and then join(puts) the string " " actually space
# between them. They are the same for all strings assigned to song. I think they
# would be different if there isn't anyspace.

'''EX10


def replace(s, old, new):
    list = s.split(old)
    # print(list)
    a = new
    list = a.join(list)
    # print(list)
    return list


test(replace("Mississippi", "i", "I") == "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
test(replace(s, "om", "am") ==
     "I love spam! Spam is my favorite food. Spam, spam, yum!")

test(replace(s, "o", "a") ==
     "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
'''

'''EX11'''


def swap(x, y):      # Incorrect version
    print("before swap statement: x:", x, "y:", y)
    (x, y) = (y, x)
    print("after swap statement: x:", x, "y:", y)
    return x, y


a = ["This", "is", "fun"]
b = [2, 3, 4]
print("before swap function call: a:", a, "b:", b)
swap(a, b)
print("after swap function call: a:", a, "b:", b)

# It didnt do what we intended because Passing a list as an argument actually
# passes a reference to the list, not a copy or clone of the list.
# The values of a and b after call to swap will be the same, the wont change.
# Type visualizer python online put your code there, and check step by step.
