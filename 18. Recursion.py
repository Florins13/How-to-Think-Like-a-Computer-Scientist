import os
import sys
import turtle
from unit_tester import test
# wn = turtle.Screen()
# tom = turtle.Turtle()
# tom.speed(0)


def koch_0(t, size):
    t.forward(size)


def koch_1(t, size):
    for angle in [60, -120, 60, 0]:
        koch_0(t, size/3)
        t.left(angle)


def koch_2(t, size):
    for angle in [60, -120, 60, 0]:
        koch_1(t, size/3)
        t.left(angle)


def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)


# koch_1(tom, 400)
# Ex 1


def koch_snowflake(t, size):
    for angle in [120, 120, 0]:
        koch_2(t, size/3)
        t.right(angle)


# koch_snowflake(tom, 600)

# Ex 2
def tear(t, size):
    t.forward(size)


def tear1(t, size):
    for angle in [85, -170, 85, 0]:
        tear(t, size/3)
        t.right(angle)


def tear2(t, size):
    for angle in [85, -170, 85, 0]:
        tear1(t, size/3)
        t.right(angle)


def tear3(t, size):
    for angle in [85, -170, 85, 0]:
        tear2(t, size/3)
        t.right(angle)


def tear_cesaro(t, order, size):
    print(size)
    if order == 0:
        t.forward(size)
    else:
        for angle in [85, -170, 85, 0]:
            tear_cesaro(t, order-1, size/2)
            t.right(angle)


# tear_cesaro(tom, 3, 100)


def square(t, order, size):
    if order == 0:
        t.forward(size)
    for angle in [90, 90, 90, 90]:
        tear_cesaro(t, order-1, size)
        tom.right(angle)


# square(tom, 4, 100)

# Ex 3

def sierpinski_triunghi(t, order, size, colorChangeDepth):
    print(colorChangeDepth)
    if order == 0:
        t.forward(size)
        t.left(120)
        t.forward(size)
        t.left(120)
        t.forward(size)
        t.left(120)
    else:
        if colorChangeDepth == 0:
            t.color("red")
        sierpinski_triunghi(t, order-1, size/2, colorChangeDepth-1)
        t.penup()
        t.forward(size/2)
        t.pendown()
        if colorChangeDepth == 0:
            t.color("blue")
        sierpinski_triunghi(t, order-1, size/2, colorChangeDepth-1)
        t.penup()
        t.left(120)
        t.forward(size/2)
        t.right(120)
        t.pendown()
        if colorChangeDepth == 0:
            t.color("green")
        sierpinski_triunghi(t, order-1, size/2, colorChangeDepth-1)
        t.penup()
        t.right(120)
        t.forward(size/2)
        t.left(120)
        t.pendown()


# sierpinski_triunghi(tom, 3, 300, 0)

# wn.mainloop()


# Ex 5

def recursive_min(list):
    smallest = 0
    first_test = True
    for number in list:
        if type(number) == type([]):
            # val gets the smallest number from return smallest and gets compared to smallest in the if statement
            val = recursive_min(number)
        else:
            val = number
        # first_True that means by rules if first statement is True the next code is not evaluated and it executes the code inside the block.
        if first_test == True or val < smallest:
            smallest = val
            first_test = False
    return smallest


# test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
# test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
# test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
# test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)

# Ex 6


def count(target, list):
    aduna = 0
    for number in list:
        if number == target:
            aduna += 1
            #print(number, aduna)
        if type(number) == type([]):
            aduna += count(target, number)
    return aduna


# test(count(2, []) == 0)
#test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
# test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
# test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
# test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
# test(count("a",
#            [["this", ["a", ["thing", "a"], "a"], "is"], ["a", "easy"]]) == 4)

# EX 7
def flatten(list):
    simple = []
    for elem in list:
        if type(elem) == type([]):
            simple += flatten(elem)
        else:
            simple.append(elem)
    return simple


#test(flatten([2, 9, [2, 1, 13, 2], 8, [2, 6]]) == [2, 9, 2, 1, 13, 2, 8, 2, 6])
# test(flatten([[9, [7, 1, 13, 2], 8], [7, 6]]) == [9, 7, 1, 13, 2, 8, 7, 6])
# test(flatten([[9, [7, 1, 13, 2], 8], [2, 6]]) == [9, 7, 1, 13, 2, 8, 2, 6])
# test(flatten([["this", ["a", ["thing"], "a"], "is"], ["a", "easy"]]) ==
#      ["this", "a", "thing", "a", "is", "a", "easy"])
# test(flatten([]) == [])

# Ex 8

def fib(n):
    a = 0
    b = 1
    if n == 0:
        return a
    if n == 1:
        return b
    else:
        for i in range(2, n+1):
            x = a + b
            a = b  # this a stores the number of last b
            b = x  # b gets the new value
            #print("x:", x, " a:", a, " b:", b, i)
        print(b)


# fib(5)

# Ex 9

sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())


def recursion_depth(number):
    print("{0}, ".format(number), end="")
    recursion_depth(number + 1)


# recursion_depth(0) # print this and modify setrecursionlimit and you will understand.

# Ex 10


def get_dirlist(path):
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


def print_files(path):
    list = []
    dirlist = get_dirlist(path)
    for file in dirlist:
        fullpath = (os.path.join(path, file))
        if os.path.isfile(fullpath):
            list.append(fullpath)
        if os.path.isdir(fullpath):
            list += print_files(fullpath)
    return list


# get_dirlist("C:/Users/sofin/Desktop/Exercise10")
result = print_files(r"C:\Users\sofin\Desktop\Exercise10")


def result_ontextfile():
    myfile = open(r"C:\Users\sofin\Desktop\Exercise10\subjects.txt", "w")
    for i in result:
        myfile.write(i + "\n")
    myfile.close()


# This script basically writes the list with path of files in a text document.
result_ontextfile()


# Ex 11

get_dirlist(r"C:\Users\sofin\Desktop\Director")


def create_paths(path):
    list = []
    dirlist = get_dirlist(path)
    for i in dirlist:
        fullpath = (os.path.join(path, i))
        list.append(fullpath)
        if os.path.isdir(fullpath):
            list += create_paths(fullpath)
    return list


list_path = create_paths(r"C:\Users\sofin\Desktop\Director")

print(list_path)


def create_files(list):
    for i in list:
        myfile = open(i+"\emptyfile.txt", "w")
        myfile.close()


def remove_files(list):
    for i in list:
        os.remove(i)


# create_files(list_path)
# remove_files(list_path)
