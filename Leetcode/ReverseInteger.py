class Solution(object):
  def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    sign = ""
    if x >= 0:
      quo = x
    else:
      quo = -x
      sign = "-"
    record = ""
    while quo >= 10:
      record += str(quo % 10)
      quo = quo // 10
    record += str(quo)
    quo = int(sign + record)
    if quo > 2147483647 or quo < -2147483648:
      return 0
    return quo

if __name__ == "__main__":
  sol = Solution()
  testcase = [123, -123, 10, 1534236469]
  for x in testcase:
    print sol.reverse(x)