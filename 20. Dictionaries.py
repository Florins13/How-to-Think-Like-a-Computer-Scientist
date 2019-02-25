# Ex 1


from unit_tester import test


def alpha_order(sentence):
    letter_counts = {}
    for letter in sentence.lower():
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    if " " in letter_counts:
        del letter_counts[" "]
    return letter_counts


dictionary = alpha_order("ThiS is String with Upper and lower case Letters")


def table(dict):
    for key in sorted(dict):
        print(key, dict[key])


# table(dictionary)

# Ex 2
# a. >>> 35
# b. >>> 0,1,2,3 = 4
# c. >>> True
# d. >>> Hmm, i dont know adds an empty pair I guess. ---> We get an KeyError.
# e. >>> I think its false, pears is empty, I think we get some kind of error here. ---> Actually returns 0.
# f. >>> prints a sorted list of keys from d.
# g. >>> delete apples in d, and apples in d will be False.


def add_fruit(inventory, fruit, quantity=0):
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity
    return inventory


# new_inventory = {}
# add_fruit(new_inventory, "strawberries", 10)
# test("strawberries" in new_inventory)
# test(new_inventory["strawberries"] == 10)
# add_fruit(new_inventory, "strawberries", 25)
# test(new_inventory["strawberries"] == 35)
# add_fruit(new_inventory, "mere", 30)
# test("mere" in new_inventory)
# add_fruit(new_inventory, "mere", 70)
# add_fruit(new_inventory, "pere", 70)
# print(new_inventory)

# Exercise 3
# Solution is on the file alice_words.py
