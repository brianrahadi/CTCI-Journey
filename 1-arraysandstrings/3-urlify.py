# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional Characters, and that you are given the "true" length of the string
import unittest

def urlify(string: str, length: str) -> str:
    char_list = list(string)
    new_index = len(char_list)

    print(char_list)
    for i in reversed(range(length)):
        if char_list[i] == " ":
            char_list[new_index - 3 : new_index] = "%20"
            new_index -= 3
        else:
            char_list[new_index - 1] = char_list[i]
            new_index -= 1

    return "".join(char_list[new_index:])

# First, we make strings into an array of chars since strings are immutable and initialize a new index variable that is the length of the string (with whitespaces).
# Run a for loop reversedly from the true length (input) to 0
# if char at i is whitespace, then from i - 3 to i will be %20, subtract new index by 3
# else, we just need to move the character, which is assign char at new index - 1 to i, subtract new index by 1
# return the char of arrays as string starting from new index after the loop
# Time Complexity: O(n) and n is the true length of the string (for loop)
# Space complexity: O(m) and this m is the length of the string with whitespaces