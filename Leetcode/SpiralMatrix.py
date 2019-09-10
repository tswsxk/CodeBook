class Solution(object):
  def spiralOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix:
      return matrix
    res = []
    m = len(matrix)
    n = len(matrix[0])
    upbound, downbound, leftbound, rightbound = 0, m - 1, 0, n - 1
    while True:
      # right move
      if len(res) == m * n:
        break
      res += matrix[upbound][leftbound: rightbound + 1]
      upbound += 1

      # down move
      if len(res) == m * n:
        break
      res += [row[rightbound] for row in matrix[upbound:downbound + 1]]
      rightbound -= 1

      # left move
      if len(res) == m * n:
        break
      res += list(reversed(matrix[downbound][leftbound:rightbound + 1]))
      downbound -= 1

      # up move
      if len(res) == m * n:
        break
      res += [row[leftbound] for row in reversed(matrix[upbound:downbound + 1])]
      leftbound += 1

    return res

if __name__ == "__main__":
  test = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
  sol = Solution()
  print sol.spiralOrder(test)
