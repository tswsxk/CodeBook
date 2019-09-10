class Solution(object):
  def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    ind = 0
    pos = 0
    while ind < len(nums):
      if nums[ind] == val:
        ind += 1
      else:
        nums[pos] = nums[ind]
        ind += 1
        pos += 1
    return pos

if __name__ == "__main__":
  sol = Solution()
  sol.removeElement([4,3,2,1], 3)