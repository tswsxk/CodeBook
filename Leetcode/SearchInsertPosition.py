class Solution(object):
  def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    head = 0
    tail = len(nums) - 1
    while head < tail - 1:
      mid = (head + tail + 1) // 2
      if nums[mid] == target:
        return mid
      elif nums[mid] < target:
        head = mid
      else:
        tail = mid
    if nums[head] >= target:
      return head
    elif nums[tail] < target:
      return tail + 1
    else:
      return tail

if __name__ == "__main__":
  sol =Solution()
  print sol.searchInsert([1, 2], 0)

