class Solution(object):
  def divide(self, dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    if dividend == 0:
      return 0
    if divisor == 0:
      return -1
    if (dividend > 0 and divisor >0) or (dividend < 0 and divisor < 0):
      posTag = True
    else:
      posTag = False
    res = 0
    re = abs(dividend)
    while re >= abs(divisor):
      sub = abs(divisor)
      num = 1
      while re > (sub << 1):
        sub = sub << 1
        num = num << 1
      re -= sub
      res += num
    if re < 0:
      res -= 1
    if not posTag:
      res = -res
    if res > 2147483647:
      return 2147483647
    elif res < -2147483648:
      return -2147483648
    return res

if __name__ == "__main__":
  sol = Solution()
  x = (5, 2)
  sol.divide(x[0], x[1])