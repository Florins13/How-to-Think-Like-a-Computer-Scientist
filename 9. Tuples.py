import math


def tuple_function(b, c, d):
    name = b
    age = c
    studies = d
    chunk = b + c + d
    print(name, age, studies, chunk)
    print(name, "has age of:", age, "and is studying:", studies)


tuple_function(("bob", "ana"), (22, 23), ("CS", "chemistry"))


def f(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)


print(f(25))
'''
A tuple lets us “chunk” together related information and use it as a single thing
'''
# Is a pair a generalization of a tuple, or is a tuple a generalization of a pair?
# I would say tuple is a generalization of a pair. :D


# Is a pair a kind of tuple, or is a tuple a kind of pair?
# A tuple is a kind of pair.
