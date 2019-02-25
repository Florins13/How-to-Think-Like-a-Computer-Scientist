import string
import os
import sys


def alpha_order(sentence):
    word_counts = {}
    for word in sentence:
        word.lower()
        word_counts[word] = word_counts.get(word, 0) + 1
    if "" in word_counts:
        del word_counts[""]
    return word_counts


def read_file(file):
    list = []
    f = open(file, "r")
    content = f.read()
    f.close()
    words = content.split()
    words.sort()
    words = [''.join(c for c in s if c not in string.punctuation) for s in words]
    list = [w.lower() for w in words]
    dictionary = alpha_order(list)
    return dictionary


something = read_file("AliceInWonderland.txt")


def table(dict):
    b = 0
    for key in sorted(dict):
        print(key, "\t", "\t", dict[key])
        if len(key) > b:
            a = key
            b = len(key)
    print("The longest word is", a, "and has the length of", b)


def create_file(path, dict):
    myfile = open(path, "w")
    myfile.write("Word              Count\n")
    myfile.write("=======================\n")
    b = 0
    for key in sorted(dict):
        #myfile.write(key + str(dict[key])+"\n")
        myfile.write("%-20s %s" % (key, str(dict[key])) + "\n")
        if len(key) > b:
            a = key
            b = len(key)
    myfile.write("The longest word is " + str(a) + "and has the length of " + str(b))
    myfile.close()


print("The word 'alice' appears ", something['alice'], "times in the book.")
# table(something)
create_file("alice_words.txt", something)
