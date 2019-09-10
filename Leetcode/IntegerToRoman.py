class Solution(object):
  def intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """
    ordNumMap = {0: "I", 1: "X", 2: "C", 3: "M"}
    bigNumMap = {0: "V", 1: "L", 2: "D"}
    numStr = str(num)
    res = ""
    l = len(numStr) - 1
    for p, c in enumerate(numStr):
      n = int(c)
      i = l - p
      if n == 0:
        pass
      elif n <= 3:
        res += n * ordNumMap[i]
      elif n == 4:
        res += (ordNumMap[i] + bigNumMap[i])
      elif n < 9:
        res += (bigNumMap[i] + (n - 5) * ordNumMap[i])
      else:
        res += (ordNumMap[i] + ordNumMap[i + 1])
    return res
if __name__ == "__main__":
  sol = Solution()
  testcase = [123, 1, 9, 1999, 89]
  for x in testcase:
    print sol.intToRoman(x)