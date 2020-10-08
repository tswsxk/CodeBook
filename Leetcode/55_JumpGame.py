class Solution(object):
  def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    l = len(nums)
    if l <= 1:
      return True
    head, tail = 1, nums[0]
    while tail < l - 1:
      if tail < head:
        return False
      head, tail = tail + 1, max([head + i + num for i, num in enumerate(nums[head:tail + 1])])
    return True

if __name__ == "__main__":
  sol = Solution()
  sol.canJump([2, 0, 0])