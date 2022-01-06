# 1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0

def zero_matrix(arr: list[int]) -> list[int]:
  rows = set()
  cols = set()

  m = len(arr)
  n = len(arr[0])

  for i in range(m):
    for j in range(n):
      if arr[i][j] == 0:
        rows.add(i)
        cols.add(j)
  
  for i in range(m):
    for j in range(n):
      if (i in rows) or (j in cols):
        arr[i][j] = 0

  return arr

# Firstly, we can't immediately make it all to zero at first. Because after that, the zeroed element will zero his rows and columns again after checking. So, we need to check all of the zero coordinate first before making all of it to be zero. My first approach was to store all the coordinates and zero all of it. I just realized there could be many overlapping coordinates and it will be slower, so using set for rows and cols will be faster.

# Explanation: First, we need to have sets for row and cols (this can also be boolean array or even dict). We will iterate through the array and if it has 0, add its row to row set and its col to col set. After the first n^2 loop ends, we make another n^2 loop to check if the row is in row set or col is in col set, if true, make it to be zero. 

# Time Complexity: O(mn) since we need to iterate through MxN array
# Space Complexity: O(m) or O(n) for the row or cols set