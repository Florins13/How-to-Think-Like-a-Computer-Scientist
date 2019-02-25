from unit_tester import test
import string


def cleanword(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct


#test(cleanword("what?") == "what")
#test(cleanword("'now!'") == "now")
#test(cleanword("?+='w-o-r-d!,@$()'") == "word")


def has_dashdash(s):
    a = s.find("--")
    if a != -1:
        return True
    else:
        return False


# test(has_dashdash("distance--but"))
#test(not has_dashdash("several"))
# test(has_dashdash("spoke--"))
# test(has_dashdash("distance--but"))
#test(not has_dashdash("-yo-yo-"))

s = "Now is the time!  'Now', is the time? Yes, now."


def extract_words(s):
    list = " ".join(s.split("--"))
    list1 = list.lower()
    list2 = cleanword(list1)
    list3 = list2.split()
    print(list3)
    return list3


# test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
    # ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now'])
# test(extract_words("she tried to curtsey as she spoke--fancy") ==
    # ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy'])


def wordcount(word, list):
    count = 0
    for s in list:
        if word == s:
            count += 1
    return count


#test(wordcount("now", ["now", "is", "time", "is", "now", "is", "is"]) == 2)
#test(wordcount("is", ["now", "is", "time", "is", "now", "the", "is"]) == 3)
#test(wordcount("time", ["now", "is", "time", "is", "now", "is", "is"]) == 1)
#test(wordcount("frog", ["now", "is", "time", "is", "now", "is", "is"]) == 0)


def wordset(list):
    new_list = []
    for i in sorted(list):
        new_elem = i
        if new_elem not in new_list:
            new_list.append(new_elem)
    print(new_list)
    return new_list


# test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
    # ["is", "now", "time"])
# test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
    # ["I", "a", "am", "is"])
# test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
    # ["a", "am", "are", "be", "but", "is", "or"])

def longestword(list):
    greatest = 0
    for i in list:
        if len(i) >= greatest:
            greatest = len(i)
    # print(greatest)
    return greatest


test(longestword(["a", "apple", "pear", "grape", "lol"]) == 5)
test(longestword(["a", "am", "I", "be", "s"]) == 2)
test(longestword(["this", "supercalifragilisticexpialidocious", "sos"]) == 34)
test(longestword([]) == 0)
