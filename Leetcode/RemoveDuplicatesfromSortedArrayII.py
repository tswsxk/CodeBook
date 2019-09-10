class Solution(object):
  def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ind = 0
    res = []
    twice_tag = False
    while ind < len(nums):
      if res and nums[ind] == res[-1]:
        if twice_tag:
          pass
        else:
          res.append(nums[ind])
          twice_tag = True
      else:
        twice_tag = False
        res.append(nums[ind])
      ind += 1
    nums[:len(res)] = res
    return len(res)

if __name__ == "__main__":
  sol = Solution()
  sol.removeDuplicates([3, 3, 4, 5, 6, 6, 6])