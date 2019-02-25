import string
import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


'''Ex 1
>>> "Python"[1]
'y'
>>> "Strings are sequences of characters."[5]
'g'
>>> len("wonderful")
9
>>> "Mystery"[:4]
'Myst'
>>> "p" in "Pineapple"
True
>>> "apple" in "Pineapple"
True
>>> "pear" not in "Pineapple"
True
>>> "apple" > "pineapple"
False
>>> "pineapple" < "Peach"
False
>>> "pineapple" > "Peach"
True
'''

'''Ex 2'''


def names():
    prefixes = "JKLMNOPQ"
    suffix = "ack"
    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            print(letter + "u" + suffix)
        else:
            print(letter + suffix)


'''Ex 3'''


def count_letters(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

# banana = "banana"
# letter = 'a'
# count_letters(banana, letter)
# print(count_letters(banana, letter))
# print(count_letters('banana', 'a'))


'''Ex 4'''


def count_letters_rewrite(string, letter, optional=0):
    count = 0
    position = string.find(letter, optional)
    print(position)  # atentie, aici merge printul deoarece nu intra in loop
    while position != -1:
        position = string.find(letter, position + 1)  # trecem pe la fiecare litera
        # fals, aceasta linie nu este executata deoarece position == -1, vezi mai sus.
        print(position)
        count += 1
    return count
# print(count_letters_rewrite('portocala', 'x'))
# string = 'bicicleta'
# print(string.find('x'))


'''Ex 5'''
python_string = """
Pythons are constrictors, which means that they will 'squeeze' the life
out of their prey. They coil themselves around their prey and with
each breath the creature takes the snake will squeeze a little tighter
until they stop breathing completely. Once the heart stops the prey
is swallowed whole. The entire animal is digested in the snake's
stomach except for fur or feathers. What do you think happens to the fur,
feathers, beaks, and eggshells? The 'extra stuff' gets passed out as ---
you guessed it --- snake POOP! """


def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct


# print(new_python_string)


def clean_up(string, letter):
    count_words = 0
    words_letter_e = 0
    new_python_string = remove_punctuation(string).split()
    for a in new_python_string:
        count_words += 1
        if letter in a:
            words_letter_e += 1
    percentage = (words_letter_e * 100) / count_words
    print(new_python_string)
    final = "Your text cotains {0} words, of which {1} ({2:.2f}%) contain an \"{3}\".".format(
        count_words, words_letter_e, percentage, letter)
    print(final)

# clean_up(python_string, 'e')


'''EX6 kind of finished'''


def mult_table():
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    x5 = 0
    x6 = 0
    x7 = 0
    x8 = 0
    x9 = 0
    x10 = 0
    x11 = 0
    x12 = 0
    layout = "{0:>2}:{1:>6}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}{12:>4}"
    print(layout.format("", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"))
    print(layout.format("", "----------", "------", "-----",
                        "------", "-----", "-----", "-----", "--------", "", "", "", ""))
    for i in range(1, 13):
        x1 = x1 + 1
        x2 = x2 + 2
        x3 = x3 + 3
        x4 = x4 + 4
        x5 = x5 + 5
        x6 = x6 + 6
        x7 = x7 + 7
        x8 = x8 + 8
        x9 = x9 + 9
        x10 = x10 + 10
        x11 = x11 + 11
        x12 = x12 + 12
        print(layout.format(i, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12))


def tabletable():
    layout = "{0:>2}:{1:>6}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}"
    print(layout.format("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
    for i in range(1, 11):
        print(layout.format(i, 2*i, 3*i, 4*i, 5*i, 6*i, 7*i, 8*i, 9*i, 10*i, 10*i))


# tabletable()

'''EX 7'''


def reverse(string):
    new_string = ""
    x = 0
    while x < len(string):
        x += 1
        new_string = new_string + string[-x]
    print(new_string)
    return new_string


# reverse("Florin")
'''EX 8'''


def mirror(string):
    mirror_string = ""
    x = 0
    while x < len(string):
        x += 1
        mirror_string = mirror_string + string[-x]
    new_string = string + mirror_string
    print(new_string)
    return new_string


# mirror("Florica")

'''EX 9'''


def remove_letter(letter, string):
    new_string = ""
    x = 0
    for char in string:
        if letter != char:
            new_string += char
    return new_string


'''Ex 10'''


def is_palindrome(string):
    new_string = ""
    x = 0
    while x < len(string):
        x += 1
        new_string = new_string + string[-x]
    if string == new_string:
        return True
    else:
        return False


'''EX 11'''


def count(substring, stringg):
    count = 0
    x = 0
    while x < len(stringg):
        if (stringg.find(substring, x, x+len(substring)) != -1):
            count += 1
        x += 1
    return count


'''EX 12'''


def remove(argument, string):
    x = 0
    new_string = ""
    slice1 = 0
    slice2 = len(argument)
    while x < len(string):
        if (string.find(argument) != -1):
            slice1 = string.find(argument)
            new_string = string[0:slice1] + string[slice1+slice2:]
        else:
            return string
        x += 1
    return new_string


'''EX 13'''


def remove_all(argument, string):
    remove(argument, remove(argument, string))


# print(remove("an", (remove("an", "banana"))))
test(remove_all("an", "banana") == "ba")
test(remove_all("cyc", "bicycle") == "bile")
test(remove_all("iss", "Mississippi") == "Mippi")
test(remove_all("eggs", "bicycle") == "bicycle")
