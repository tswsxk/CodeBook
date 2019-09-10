class Solution(object):
  def uniquePathsWithObstacles(self, obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    for row in obstacleGrid:
      for col, num in enumerate(row):
        if num == 1:
          row[col] = -1
        else:
          row[col] = -2
    def findPath(x, y):
      if x == m - 1 and y == n - 1 and obstacleGrid[x][y] != -1:
        return 1
      elif x >= m or y >= n:
        return 0
      else:
        if obstacleGrid[x][y] == -1:
          return 0
        elif obstacleGrid[x][y] >= 0:
          return obstacleGrid[x][y]
        else:
          res = findPath(x + 1, y) + findPath(x, y + 1)
          obstacleGrid[x][y] = res
          return res
    return findPath(0, 0)

if __name__ == "__main__":
  sol = Solution()
  sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])