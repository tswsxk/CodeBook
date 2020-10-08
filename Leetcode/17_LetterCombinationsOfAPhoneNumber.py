class Solution(object):
  def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if len(digits) == 0:
      return []
    numMap = {1: ["*"], 2: ["a", "b", "c"], 3: ["d", "e", "f"],
              4: ["g", "h", "i"], 5: ["j", "k", "l"], 6: ["m", "n", "o"],
              7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"],
              0: [" "]}
    record = []
    res = []
    for n in digits:
      num = int(n)
      cs = numMap[num]
      record.append(cs)
    def getStr(ind, rec, rs):
      if ind >= len(rec):
        res.append(rs)
        return
      for x in rec[ind]:
        rs += x
        getStr(ind + 1, rec, rs)
        rs = rs[:-1]
    getStr(0, record, "")
    return res
if __name__ == "__main__":
  sol = Solution()
  testcase = ["012", "123", "812", "", "223"]
  for x in testcase:
    print sol.letterCombinations(str(x))

