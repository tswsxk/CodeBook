class Solution(object):
  def solveNQueens(self, n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    ress = []
    locs = [-1] * n
    checkarray = [[True] * n,
                  [True] * (2 * n - 1),
                  [True] * (2 * n - 1)]
    def put(dep, checkarray):
      if dep == n:
        ress.append(["." * loc + "Q" + "." * (n - loc - 1) for loc in locs])
        return
      for i in range(n):
        if checkarray[0][i] and checkarray[1][dep+i] and checkarray[2][dep-i+n-1]:
          checkarray[0][i], checkarray[1][dep + i], checkarray[2][dep - i + n - 1] = False, False, False
          locs[dep] = i
          put(dep+1,checkarray)
          checkarray[0][i], checkarray[1][dep + i], checkarray[2][dep - i + n - 1] = True, True, True
    put(0, checkarray)
    return ress

if __name__ == "__main__":
  sol = Solution()
  sol.solveNQueens(1)