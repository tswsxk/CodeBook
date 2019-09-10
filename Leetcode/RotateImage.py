class Solution(object):
  def rotate(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for x in range((n + 1) // 2):
      for y in range(n  // 2):
        cor = [[x, y], [n - y - 1, x], [n - x - 1, n - y - 1], [y, n - x - 1]]
        matrix[cor[0][0]][cor[0][1]], matrix[cor[1][0]][cor[1][1]], \
        matrix[cor[2][0]][cor[2][1]], matrix[cor[3][0]][cor[3][1]] = \
        matrix[cor[1][0]][cor[1][1]], matrix[cor[2][0]][cor[2][1]], \
        matrix[cor[3][0]][cor[3][1]], matrix[cor[0][0]][cor[0][1]]

if __name__ == "__main__":
  sol = Solution()
  sol.rotate([[1,2,3],[4,5,6],[7,8,9]])