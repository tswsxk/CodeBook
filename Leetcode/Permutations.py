class Solution(object):
  def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ress = []
    def permute_recursive(nums, res):
      if not nums:
        ress.append(res)
      else:
        for i in range(len(nums)):
          permute_recursive(nums[:i] + nums[i+1:], res + [nums[i]])
    permute_recursive(nums, [])
    return ress