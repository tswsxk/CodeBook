class Solution(object):
  def myAtoi(self, str):
    """
    :type str: str
    :rtype: int
    """
    str = str.strip()
    res = ""
    negsign = True
    possign = True
    for i,c in enumerate(str):
      if c <= '9' and c >= '0':
        res += c
      elif negsign and c == "-" and i == 0:
        res += c
        negsign = False
      elif possign and c == "+" and i == 0:
        res += c
        possign = False
      else:
        break
    if len(res) == 0 or res == "-" or res == "+":
      return 0
    else:
      num = int(res)
      if num > 2147483647:
        num = 2147483647
      elif num < -2147483648:
        num = -2147483648
      return num
if __name__ == "__main__":
  sol = Solution()
  testcase = ["  - 321", "  -0012a42", "0", "-1", "0910920", "", "++++---", "0928+910", "+", "-", "]"]
  for x in testcase:
    print sol.myAtoi(x)