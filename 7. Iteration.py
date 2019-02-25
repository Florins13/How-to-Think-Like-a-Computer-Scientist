# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      florins
#
# Created:     25/12/2018
# Copyright:   (c) florins 2018
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import turtle
import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


# def test_suite():

def seq3np1(n):
    """ Print the 3n+1 sequence from n,
        terminating when it reaches 1.
    """
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    print(n, end=".\n")


def num_zero_and_five_digits(n):
    count = 0
    while n > 0:
        digit = n % 10
        if digit == 0 or digit == 5:
            count = count + 1
        n = n // 10
    return count

# EX1


def odd_numbers(n):
    count = 0
    for a in n:
        if a % 2 != 0:
            count += 1
    print(count)
    return count

# EX2


def sum_up(n):
    count_list = 0
    for a in n:
        if a % 2 == 0:
            count_list += a
    return count_list

# EX 3


def sum_up_negative(n):
    count_negative = 0
    for a in n:
        if a < 0:
            count_negative += a
    return count_negative

# EX 4


def count_words_5(n):
    count = 0
    for a in n:
        if len(a) == 5:
            count += 1
    print(count)
    return count

# Ex 5

# --neintelegere, am crezut ca nu trebuie adunat primul numar par.


def sum_even_n(n):
    sum = 0
    first_ocurrence = True
    for a in n:
        sum += a
        if a % 2 == 0 and first_occurence == True:
            sum = sum - a
            first_occurence = False
    print(sum)
    return sum

# --varianta corecta -- oprestete la primul numar par


def sumexclude(data):
    "Sum all the elements in a list up to but not including the first even number."
    count = 0
    for i in data:
        if i % 2 == 0:
            break
        count += i
    print(count)
    return count

# EX 6


def sum_all_elem(n):
    count = 0
    for a in n:
        count += 1
        if a == "sam":
            break
    return count

# EX 7


def sqrt(n):
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        print("approx  =  ", approx)
        print("better  =  ", better)
        if abs(approx - better) < 0.001:
            print("better 1 =  ", better)
            return better

        approx = better


# EX 8


def print_multiples(n, high):  # argumentele n=1 si high = 2
    for i in range(1, high+1):  # i intre 1 si 3
        print(n * i, end="   ")  # printeaza n*i=1*1,1*2 spatiu
    print()


def print_mult_table(high):  # avem un parametru high, 2 spre ex
    for i in range(1, high+1):  # plecam de la 2 pana la 3
        print_multiples(i, i+1)  # printam i=1,2 si i+1 = 2,3


#print_multiples(1, 2)
#print_multiples(1, 3)
#print_multiples(1, 4)
#print_multiples(1, 5)
# print_mult_table(4)

# EX 9


def print_triungular_numbers(n):
    for x in range(1, n+1):
        print(x, "\t", int(x*(x+1)/2))


# EX 10

def is_prime(n):
    if n % 2 != 0 and n % 3 != 0 and n > 2 and n % 5 != 0:
        return True
    else:
        return False


# EX11
'''
wn = turtle.Screen()
tess = turtle.Turtle()

data = [(160, 20), (-43, 10), (270, 8), (-43, 12)]


def pirate_drunk(list):
    for (x, y) in list:
        print("Y = ", y)
        tess.forward(y)
        print("X = ", x)
        tess.right(x)
# pirate_drunk(data)


# EX12
#pairlist = [(100, 90), (100, 90), (100, 90), (100, 135), (141, 90), (70, 90), (70, 90), (141, 90)]

# EX 13
pairlist1 = [(0, 135), (70, 90), (141, 90), (70, 90), (141, -135), (100, -90),
             (100, -90), (100, -135), (141, 90), (70, 90), (70, 45), (100, 0)]

# 1,2,5 si 6 grafic eulerian


def shape(list):
    for (f, a) in list:
        tess.forward(f)
        tess.left(a)
        tess.speed(1)


shape(pairlist1)
wn.mainloop()
'''
# EX 14


def num_digits(n):
    count = 0
    while True:
        count = count + 1    # 1 --> 710//10=71, 2 --> 71//10 = 7, 3 --> 7//10=0, BREAK
        # print(count)
        # print(n)
        n = n // 10
        if n == 0 or n == -1:
            break
    print(count)
    return count


# EX15


def num_even_digits(n):
    count = 0
    while True:
        print(n)
        if n % 2 == 0:
            count = count + 1
            print("Aici avem + 1")
        n = n // 10
        if n == 0 or n == -1:
            break
    return count

# EX6


def sum_of_squares(xs):
    count = 0
    for a in xs:
        count = count + a**2
    return count


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """


test_suite()

# Purpose:
#
# Author:      florins
#
# Created:     26/12/2018
# Copyright:   (c) florins 2018
# Licence:     <your licence>
# -------------------------------------------------------------------------------

# Your friend will complete this function

# Last EXO


def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1, 2)
    print("Human plays first={0},  winner={1} "
          .format(human_plays_first, result))
    return result


def play(result1):
    counthuman = 0
    countcomputer = 0
    countdraws = 0
    winingpercentage = 0
    while True:
        result1 = play_once(print(input(
            "Type \"True\" if you want to play first or \"False\" if you want the computer to start first.")))
        print(result1)
        if result1 == 0:
            countdraws = countdraws + 1
            winingpercentage = ((counthuman + 0.5*countdraws) /
                                (countcomputer+countdraws+counthuman))*100
            print("game drawn!")
            print("Current draws are: ", countdraws)
            print("The wining % for human is: ", winingpercentage, "%")
            newgame = input("Do you want to play again? yes/no")

        if result1 == -1:
            counthuman = counthuman + 1
            print("I win!")
            print("Human won ", counthuman, " times.")
            newgame = input("Do you want to play again? yes/no")

        if result1 == 1:
            countcomputer = countcomputer + 1
            print("Computer wins!")
            print("Computer won ", countcomputer, " times.")
            newgame = input("Do you want to play again? yes/no")

        if newgame == "":
            print("Goodbye")
            break

        if newgame == "yes":
            continue

        if newgame == "no":
            print("Goodbye")
            break
        else:
            break


# play(True)
