# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in image is 4 bytes, write a method to rotate the image by 90 degrees.
import unittest
from copy import deepcopy
# [1, 2, 3]     [7, 4, 1]
# [4, 5, 6] --> [8, 5, 2]
# [7, 8, 9]     [9, 6, 3]

# first row becomes last column
# second row becomes second to last column
# last row becomes first column

# (0, 0) -> (0, 2)
# (0, 1) -> (1, 2)
# (0, 2) -> (2, 2)

# (1, 0) -> (0, 1)
# (1, 1) -> (1, 1)
# (1, 2) -> (2, 1)

# (2, 0) -> (0, 0)
# (2, 1) -> (1, 0)
# (2, 2) -> (2, 0)

# O(n^2) time, O(n^2) space. THIS IS NOT EFFICIENT
def rotate_matrix_space(arr: list[int]) -> list[int]:
  n = len(arr)

  ans = [[0] * n for i in range(n)]


  for i in range(n):
    for j in range(n):
      ans[j][n - 1 - i] = arr[i][j]
  
  return ans

# O(n^2) time, O(1) space
# 1 -> Transpose matrix
# 2 -> flip horizontally start
def rotate_matrix(arr: list[int]) -> list[int]:
  n = len(arr)

  for i in range(n):
    for j in range(i+1, n):
      temp = arr[i][j]
      arr[i][j] = arr[j][i]
      arr[j][i] = temp

  for i in range(n):
    for j in range(n//2):
      temp = arr[i][j]
      arr[i][j] = arr[i][n-1-j]
      arr[i][n-1-j] = temp

  return arr

arr = [[1,2,3],[4,5,6],[7,8,9]]

print(rotate_matrix(arr))

# TIL: Just realized initializing 2d array like this -> [[0] * n] * n -> causes memory link
# I did take a look at github's solution and it was way harder. I can do it with the space, but not in-place. Found the solution of in-place from https://www.youtube.com/watch?v=IdZlsG6P17w&ab_channel=NickWhite
# Explanation (in-place): First, we need to transpose the matrix -> swap(arr[i][j], arr[j][i]) and then we can flip each row horizontally, so swap(arr[i][0], arr[i][n-1]), swap(arr[i][1], arr[i][n-2]), .... This will make the matrix to be rotated 90 degree clockwise.