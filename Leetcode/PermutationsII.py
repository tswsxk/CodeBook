class Solution(object):
  def permuteUnique(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ress = []
    def permute_rec(nums, res):
      if not nums:
        ress.append(res)
      else:
        level_set = set()
        for i in range(len(nums)):
          if nums[i] in level_set:
            pass
          else:
            level_set.add(nums[i])
            permute_rec(nums[:i] + nums[i+1:], res + [nums[i]])
    permute_rec(nums, [])
    return ress

if __name__ == "__main__":
  sol = Solution()
  sol.permuteUnique([1,1,2])