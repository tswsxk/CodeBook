class Solution(object):
  def totalNQueens(self, n):
    """
    :type n: int
    :rtype: int
    """
    locs = [-1] * n
    checkarray = [[True] * n,
                  [True] * (2 * n - 1),
                  [True] * (2 * n - 1)]
    def put(dep, checkarray):
      if dep == n:
        return 1
      count = 0
      for i in range(n):
        if checkarray[0][i] and checkarray[1][dep+i] and checkarray[2][dep-i+n-1]:
          checkarray[0][i], checkarray[1][dep + i], checkarray[2][dep - i + n - 1] = False, False, False
          locs[dep] = i
          count += put(dep+1,checkarray)
          checkarray[0][i], checkarray[1][dep + i], checkarray[2][dep - i + n - 1] = True, True, True
      return count
    return put(0, checkarray)