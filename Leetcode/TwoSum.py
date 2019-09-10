class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i, n1 in enumerate(nums):
      for j, n2 in enumerate(nums):
        if n1 + n2 == target and i != j:
          return [i, j]

if __name__ == "__main__":
  sol = Solution()
  tar = sol.twoSum([3, 2, 4], 6)
  print(tar)
