class Solution(object):
  def subsets(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    def find_sets(nums, sets):
      if not nums:
        res.append(sets)
      else:
        find_sets(nums[1:], sets)
        find_sets(nums[1:], sets + [nums[0]])
    find_sets(nums, [])
    return res

if __name__ == "__main__":
  sol = Solution()
  sol.subsets([1,2])