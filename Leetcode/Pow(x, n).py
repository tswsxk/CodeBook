class Solution(object):
  def myPow(self, x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 0 or x == 1:
      return 1
    if x == 0:
      return 0
    neg = False
    if n < 0:
      neg = True
      n = -n

    res = 1
    count = 0
    pownum = x
    while (1 << count) <= n:
      if (n & (1 << count)) != 0:
        res *= pownum
      count += 1
      pownum *= pownum
    if neg:
      res = 1 / res
    return res

if __name__ == "__main__":
  sol = Solution()
  print sol.myPow(3, 18), pow(3, 18)