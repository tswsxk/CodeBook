class Solution(object):
  def minPathSum(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    pathrec = [[-1] * n for _ in range(m)]
    pathrec[m - 1][n - 1] = grid[m - 1][n - 1]

    def findPath(x, y):
      if x >= m or y >= n:
        return -1
      else:
        if pathrec[x][y] >= 0:
          return pathrec[x][y]
        else:
          down = findPath(x + 1, y)
          right = findPath(x, y + 1)
          if down < 0 and right < 0:
            return -1
          else:
            if down < 0:
              res = right
            elif right < 0:
              res = down
            else:
              res = min([down, right])
            pathrec[x][y] = res + grid[x][y]
            return pathrec[x][y]
    return findPath(0, 0)

if __name__ == "__main__":
  sol = Solution()
  sol.minPathSum([[1,2],[3,4]])