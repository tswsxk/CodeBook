class Solution(object):
  def uniquePaths(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    path_ref = {}
    def findPath(m, n):
      if m <= 0 or n <= 0:
        return 0
      if m == 1 or n == 1:
        return 1
      if m in path_ref and n in path_ref[m]:
        return path_ref[m][n]
      else:
        res = findPath(m - 1, n) + findPath(m, n - 1)
        if res > 0:
          if m in path_ref:
            path_ref[m][n] = res
          else:
            path_ref[m] = {n: res}
          return res
        else:
          return 0
    return findPath(m, n)

if __name__ == "__main__":
  sol = Solution()
  sol.uniquePaths(3, 3)

