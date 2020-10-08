class Solution(object):
  def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates =sorted(candidates)
    res = []
    for i in range(len(candidates)):
      if candidates[i] > target:
        break
      new_target = target - candidates[i]
      nums = candidates[0: i + 1]
      tempres = [candidates[i]]
      def findsum(tar, nums, tempres):
        if tar == 0:
          res.append(tempres)
          return
        if not nums:
          return
        # not use this number
        findsum(tar, nums[0:-1], tempres + [])
        while tar >= nums[-1]:
          tar -= nums[-1]
          tempres.append(nums[-1])
          findsum(tar, nums[0:-1], tempres + [])
      findsum(new_target, nums, tempres + [])
    return res


if __name__ == "__main__":
  sol = Solution()
  print sol.combinationSum([2,3,6,7], 7)