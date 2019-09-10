class Solution(object):
  def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    stageMap = {"I": 0, "V": 0, "X": 1, "L": 1, "C": 2, "D": 2, "M": 3}
    litStr = ["I", "X", "C", "M"]
    record = ["", "", "", ""]
    stage = 3
    for c in s:
      if stageMap[c] < stage:
        stage = stageMap[c]
      record[stage] += c
    res = ""
    stage = 3
    for s in reversed(record):
      if s:
        litnum = 0
        midnum = 0
        bignum = 0
        for c in s:
          if c == litStr[stage]:
            litnum += 1
          elif c == litStr[stage + 1]:
            bignum += 10
            litnum *= -1
          else:
            midnum += 5
            litnum *= -1
        res += str(litnum + midnum + bignum)
      else:
        res += "0"
      stage -= 1
    return int(res)

if __name__ == "__main__":
  sol = Solution()
  testcase = ["DCXXI", "CXXIII", "I", "IX", "MCMXCIX", "LXXXIX"]
  for x in testcase:
    print sol.romanToInt(x)

