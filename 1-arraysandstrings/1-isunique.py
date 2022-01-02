# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def is_unique(string: str) -> bool:
  dict = {}
  for char in string:
    if char in dict:
      return False
    dict[char] = True
  return True

# I used a hashtable for the implementation. In here, I will iterate through every character in a string while keeping a dictionary. If the char is in dictionary, it means there are duplicates of chars and return false, else we will put the char into the dictionary. After the loop, it means there's no returning false, so return true.
# I also specified input string which is a str and it returns a bool
# Time Complexity: O(n) since it iterates every character in a string
# Space Complexity: O(n) since it collects every character in the string into the dict
