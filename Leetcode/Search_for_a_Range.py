class Solution(object):
  def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    head = 0
    tail = len(nums) - 1
    if nums[head] > target or nums[tail] < target:
      return [-1, -1]
    def par_search(head, tail, target):
      if nums[head] > target or nums[tail] < target:
        return -1, -1
      elif nums[head] == target and nums[tail] == target:
        return head, tail
      elif head == tail:
          return -1, -1
      elif head == tail - 1:
        if nums[head] < target and nums[tail] == target:
          return tail, tail
        elif nums[head] == target and nums[tail] != target:
          return head, head
        else:
          return -1, -1
      mid = (head + tail + 1) // 2
      if nums[mid] == target:
        if nums[mid - 1] < target:
          resh = mid
          _, rest = par_search(mid + 1, tail, target)
          if rest == -1:
            return mid, mid
          else:
            return resh, rest
        if nums[mid + 1] > target:
          resh, _ = par_search(head, mid - 1, target)
          rest = mid
          if resh == -1:
            return rest, rest
          else:
            return resh, rest
      resh, resh2 = par_search(head, mid - 1, target)
      rest2, rest = par_search(mid + 1, tail, target)
      if resh == -1 and rest == -1:
        return -1, -1
      elif resh == -1:
        return rest2, rest
      elif rest == -1:
        return resh, resh2
      else:
        return resh, rest
    return par_search(head, tail, target)






if __name__ == "__main__":
  sol = Solution()
  print sol.searchRange([1, 1, 1, 2, 2, 2, 3, 3, 3], 1)