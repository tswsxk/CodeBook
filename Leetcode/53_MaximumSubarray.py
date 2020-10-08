class Solution(object):
  def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
      return nums[0]
    rec = []
    tmp = 0
    for num in nums:
      tmp += num
      rec.append(tmp)
    rec = [0] + rec
    minind = 0
    maxdiff = rec[1] - rec[minind]
    ind = 1
    while ind < len(rec):
      if rec[ind] - rec[minind] > maxdiff:
        maxdiff = rec[ind] - rec[minind]
      if rec[ind] < rec[minind]:
        minind = ind
      ind += 1
    return maxdiff

if __name__ == "__main__":
  sol = Solution()
  sol.maxSubArray([-2, -1])




