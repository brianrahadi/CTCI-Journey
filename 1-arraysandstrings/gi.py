# String Compression: Implement a method to perform basic string compression using the counts of repeated characters. Return original string if compressed string is not smaller. String has only uppercase and lowercase letters.
import unittest
import time

def compress_string(s: str) -> str:
  if len(s) <= 2:
    return s

  ans = ""
  current = s[0]
  count = 1
  for i in range(1, len(s)):
    if s[i] == current:
      count += 1
    else:
      ans += current + str(count)
      current = s[i]
      count = 1
  ans += current + str(count)
  return ans if len(ans) < len(s) else s

# TIL: Just realized len() func is O(1). I will keep using it and not assign it to variable.

# First, we return the string if length is less or equal to 2 (compressed is not smaller). We will declare an empty string, a current for keeping track of char, and count for current char counter. We just need to Iterate through the string from its second char. append ans with its current and counter only if char is different or the loop finishes, else we can just add the counter. Finally, we return the ans if the length of ans is truly smaller else just return the original string.
# Time Complexity: O(n) as we need to iterate through the string
# Space Complexity: O(1) no additional data structures used to keep track
