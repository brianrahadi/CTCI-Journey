# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.

from collections import Counter

def is_palindrome_permutation(string: str) -> bool:
  string = string.lower()

  counters = Counter(string) # Collect amount of all chars

  odd_exists = False

  for key in counters:
    if key != ' ' and counters[key] % 2 == 1:
      if not odd_exists:
        odd_exists = True # Middle element, 1 char can has odd amount
      else:
        return False
  return True

# First, we need to make all characters lowercase (or uppercase). I imported a dict counter to make things easy, however I can also implement it manually with a set and iterate through all the chars and store it. Then we just need to iterate through each char's amount (except amount of whitespace). If there exist an odd amount for the second time, then return false. after the loop just return true
# Time Complexity: O(n) since n is the length of the strings
# Space Complexity: O(n) since we need to use counters (same length)