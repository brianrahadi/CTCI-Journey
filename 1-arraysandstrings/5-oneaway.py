from collections import Counter

def is_one_replace_away(s1: str, s2: str) -> bool:
  edited = False
  for c1, c2 in zip(s1, s2):
    if c1 != c2:
      if edited:
        return False
      edited = True
  return True


def is_one_insert_away(s1: str, s2: str) -> bool:
  i, j = 0, 0
  len1, len2 = len(s1), len(s2)

  edited = False
  while i < len1 and j < len2:
    if s1[i] != s2[j]:
      if edited:
        return False
      edited = True
      j += 1
    else:
      i += 1
      j += 1
  return True

def is_one_edit_away(s1: str, s2: str) -> bool:
  len1 = len(s1)
  len2 = len(s2)
  if len1 == len2:
    return is_one_replace_away(s1, s2)
  elif len1 + 1 == len2:
    return is_one_insert_away(s1, s2)
  elif len2 + 1 == len1:
    return is_one_insert_away(s2, s1)
  return False

# First, we need to break down the problem of what causes the one edit away, it's mostly caused of three scenarios -> replacement, deletion, or insertion. we know that replacement means that both strings have same length. Deletion for one string is an insertion for the other string so it's technically the same (both strings only differs the length by 1). We then check the length, if it's the same, run the cases for a replace away, if length differs by 1, run the cases for one insert away.
# for one replace away, just run through the chars and return False if there's two differing chars
# for one insert away, we need to know the bigger string first, then keep 2 pointers and iterate through both of the strings, if it's different, just increment the pointer of the bigger strings.
# Time Complexity: O(n) since we will mostly be calling the length of string and iterate with pointers
# Space Complexity: O(1) no additional data structure used

