class Solution(object):
  def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    steps = [-1] * max([n + 1, 3])
    steps[1] = 1
    steps[2] = 2
    def findways(x):
      if x <= 0:
        return
      elif steps[x] > 0:
        return steps[x]
      else:
        ways = findways(x - 1) + findways(x - 2)
        steps[x] = ways
        return steps[x]
    return findways(n)