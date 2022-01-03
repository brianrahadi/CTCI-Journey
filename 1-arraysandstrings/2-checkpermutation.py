# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other

def check_permutation(s1: str, s2: str) -> bool:
  dict = {}
  for char in s1:
    if char in dict:
      dict[char] += 1
    else:
      dict[char] = 1
  
  for char in s2:
    if char in dict and dict[char] > 0:
      dict[char] -= 1
    else:
      return False
    
  return True if sum(dict.values()) == 0 else False

#  I used a hashtable (dict) to acquire the amount of each characters in s1. Alternatively, I can also use a counter which is the same. After getting all the chars in s1, I move to s2 and deduce the amount in dict if a char is found. If char is not found or the amount of char in dict is 0, we need to return false. After all the loops, one final check is required which is too sum all the values of the dict. A true permutation means it should be the same set, so all the values must be 0 and return True. If not, then s1 has way more characters and return False
# Time Complexity: O(n) which is the length of s1
# Space Complexity: O(n) which is the length of s1