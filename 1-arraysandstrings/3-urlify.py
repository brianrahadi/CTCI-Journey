# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional Characters, and that you are given the "true" length of the string
import unittest

def urlify(string, length):
    """replace spaces with %20 and removes trailing spaces"""
    char_list = list(string)
    new_index = len(char_list)

    print(char_list)
    for i in reversed(range(length)):
        if char_list[i] == " ":
            char_list[new_index - 3 : new_index] = "%20"
            new_index -= 3
            print(char_list)
        else:
            char_list[new_index - 1] = char_list[i]
            new_index -= 1

    return "".join(char_list[new_index:])

# Reserved for tomorrow