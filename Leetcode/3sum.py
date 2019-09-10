class Solution(object):
  def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:
      return []
    result = []
    nums = sorted(nums)
    for i, n1 in enumerate(nums):
      new_target = -n1
      if i == 0:
        new_nums = nums[1:]
      else:
        if n1 == nums[i-1]:
          continue
        new_nums = nums[i+1:]
      l = len(new_nums)
      left_index = 0
      right_index = l - 1
      while left_index < right_index:
        if left_index > 0 and new_nums[left_index] == new_nums[left_index-1]:
          left_index += 1
          continue
        if right_index < l - 1 and new_nums[right_index] == new_nums[right_index+1]:
          right_index -= 1
          continue
        if new_nums[left_index] + new_nums[right_index] == new_target:
          result.append([n1, new_nums[left_index], new_nums[right_index]])
          left_index += 1
          right_index -= 1
        elif new_nums[left_index] + new_nums[right_index] > new_target:
          right_index -= 1
        else:
          left_index += 1
    return result

if __name__ == "__main__":
  sol = Solution()
  res = sol.threeSum([-1,0,1,2,-1,-4])
  print(res)