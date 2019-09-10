class Solution(object):
  def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    def binsearch(head, tail, target):
      if head > tail:
        return False
      elif head == tail:
        if nums[head] == target:
          return True
        else:
          return False
      elif nums[head] < nums[tail]:
        while head <= tail:
          mid = (head + tail) // 2
          if nums[mid] == target:
            return True
          elif nums[mid] < target:
            head = mid + 1
          else:
            tail = mid - 1
        return False
      else:
        if binsearch(head, (head + tail) // 2, target):
          return True
        if binsearch((head + tail) // 2 + 1, tail, target):
          return True
        return False

    return binsearch(0, len(nums) - 1, target)

if __name__ == "__main__":
  sol = Solution()
  print sol.search([1], 1)

