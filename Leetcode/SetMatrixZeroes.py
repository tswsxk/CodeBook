class Solution(object):
  def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    zero_row = []
    zero_col = set()
    for rn, row in enumerate(matrix):
      for j, col in enumerate(row):
          if col == 0:
            zero_row.append(rn)
            zero_col.add(j)
    for rn in zero_row:
      matrix[rn] = [0 for _ in row]

    for cn in zero_col:
      for i in range(m):
        matrix[i][cn] = 0

if __name__ == "__main__":
  testlist = [1,2,3,4]
  print testlist.count(0)