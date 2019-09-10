class Solution(object):
  def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ind = 0
    while ind < len(nums):
      num = nums[ind]
      if num != ind + 1 and 1 <= num <= len(nums) and nums[num - 1] != num:
        nums[ind], nums[num - 1] = nums[num - 1], nums[ind]
      else:
        ind += 1
    i = 0
    for i, n in enumerate(nums):
      if n != i + 1:
        return i + 1
    return len(nums) + 1

if __name__ == "__main__":
  sol = Solution()
  print sol.firstMissingPositive([1, -1])