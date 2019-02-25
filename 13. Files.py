import urllib.request
from unit_tester import test

myfile = open("test.txt", "w")
myfile1 = open("test2.txt", "w")
myfile.write("My first file written from Python\n")
myfile.write("---------------------------------\n")
myfile.write("Hello, world!\n")
myfile.close()
myfile1.close()

# Ex 1


def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    listoflines = infile.readlines()
    print(type(listoflines))  # just for some help to see if you get a list
    listoflines.reverse()  # reverse the list(lines)
    for everyline in listoflines:
        outfile.write(everyline)
    infile.close()
    outfile.close()


#filter("test.txt", "test2.txt")
'''
mynewhandle = open("test.txt", "r")
while True:                            # Keep reading forever
    theline = mynewhandle.readline()   # Try to read next line
    if len(theline) == 0:              # If there are no more lines
        break  # leave the loop
    print(theline, end="")
mynewhandle.close()
'''

# Ex 2, a bit more complete than requirments, you can print by putting any word you like!


def readsnake(file, word):
    myhandler = open("snake.txt", "r")
    listoflines = myhandler.readlines()
    for line in listoflines:
        if word in line:
            print(line)
    myhandler.close()


#readsnake("snake.txt", "snake")

# Ex 3
def addnumber(oldfile, newfile):
    count = 1
    oldhandler = open(oldfile, "r")
    newhandler = open(newfile, "w")
    listoflines = oldhandler.readlines()
    for line in listoflines:
        if count < 6:
            newhandler.write(str(count) + " ")
        count += 1
        newhandler.write(line)
    oldhandler.close()
    newhandler.close()
    newhandler = open(newfile, "r")
    listofnewlines = newhandler.readlines()
    print(listofnewlines)
    newhandler.close()
    return listofnewlines


# test(addnumber("snake.txt", "numberedsnake.txt") == ['1 My first file written from Python\n', '2 ---------------------------------\n',
#                                                     '3 Hello, world!\n', '4 I have the snake!\n', 'I do not have it!\n', 'Haha, I got the snake as well!\n', 'Go away!!!'])

# Ex 4

# Just remove any numbers the list has at the beginning.


def removenumbers(oldfile, newfile):
    oldhandler = open(oldfile, "r")
    newhandler = open(newfile, "w")
    listoflines = oldhandler.readlines()
    for (index, value) in enumerate(listoflines):
        if str(index+1) in value:
            newhandler.write(value[2:])
        if str(index+1) not in value:
            newhandler.write(value)
    oldhandler.close()
    newhandler.close()
    newhandler = open(newfile, "r")
    listofnewlines = newhandler.readlines()
    print(listofnewlines)

# Its index+1 because the exercise says that list starts the numbering from 1,
# where the index starts from 0. Use print in case you dont understand.


removenumbers("numberedsnake.txt", "nonumbers.txt")
