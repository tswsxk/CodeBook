class Solution(object):
  def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ind = 0
    pos = 0
    while ind < len(nums):
      if ind > 0 and ind < len(nums) and nums[ind] == nums[ind - 1]:
        ind += 1
        continue
      nums[pos] = nums[ind]
      pos += 1
      ind += 1
    return pos

if __name__ == "__main__":
  sol = Solution()
  sol.removeDuplicates([1,2,2,2])