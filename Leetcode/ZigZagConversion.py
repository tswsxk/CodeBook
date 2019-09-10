class Solution(object):
  def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
      return s
    else:
      l = len(s)
      res = ""
      for i in range(0, numRows):
        for j in range(i, l, 2 * numRows - 2):
          res += s[j]
          if i != 0 and i != numRows - 1 and j + 2 * (numRows - 1 - i) < l:
            res += s[j + 2 * (numRows - 1 - i)]
      return res
if __name__ == "__main__":
  sol = Solution()
  testcase= [["PAYPALISHIRING", 3], ["", 2]]
  for x in testcase:
    print sol.convert(x[0], x[1])