# 1.9: String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is rotation of s1 using 1 call to isSubstring
import unittest
def is_string_rotation(s1: str, s2: str) -> bool:
  if len(s1) == len(s2) and len(s1) != 0:
    return s2 in s1 * 2 # s2 is in s1+s1,  isSubstring(s2, s1+s1)
  return False

# Since this is only the rotation of a string, two combined rotated string must have the original string in it. So, first we just need to check if the length is the same and it is not 0, then we return isSubstring(s2, s1+s1). Else return false.
# Time Complexity: O(m+n) where m is length of s1 and n is length of s2
# Space Complexity: O(m+n) since we need to do s1+s1

