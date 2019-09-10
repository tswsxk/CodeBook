class Solution(object):
  def combinationSum2(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates = sorted(candidates)
    res = []
    def findsum(canlist, target, tempres):
      if not canlist:
        return
      if canlist[0] > target:
        pass
      elif canlist[0] == target:
        res.append(tempres + [canlist[0]])
      else:
        findsum(canlist[1:], target, tempres + [])
        ind = 0
        while ind < len(canlist) - 1 and canlist[ind] == canlist[ind + 1]:
          ind += 1
        times = ind + 1
        if target >= times * canlist[0]:
          target -= times * canlist[0]
          tempres += canlist[:ind + 1]
          if target == 0:
            res.append(tempres)
            return
          else:
            findsum(canlist[ind + 1:], target, tempres + [])
    findsum(candidates, target, [])
    return res

if __name__ == "__main__":
  sol = Solution()
  print sol.combinationSum2([1, 1, 1, 1, 2, 2], 3)

