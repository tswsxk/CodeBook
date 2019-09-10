class Solution(object):
  def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    head = 0
    tail = len(nums) - 1
    def bin_search(head, tail, target):
        # division
        if head == tail:
          if target != nums[head]:
            return -1
          else:
            return head
        while head < tail - 1:
          mid = (head + tail + 1) // 2
          if nums[mid] == target:
            return mid
          elif nums[mid] < target:
            head = mid
          else:
            tail = mid
        return -1
    def par_search(head, tail, target):
      if head >= tail:
        return -1
      if nums[head] < nums[tail]:
        if nums[head] < target and target < nums[tail]:
          return bin_search(head, tail, target)
        return -1
      else:
        mid = (head + tail + 1) // 2
        if nums[mid] == target:
          return mid
        res = par_search(head, mid, target)
        if res != -1:
          return res
        res = par_search(mid, tail, target)
        if res != -1:
          return res
        return -1

    if nums[head] == target:
      return head
    if nums[tail] == target:
      return tail
    return par_search(head, tail, target)

if __name__ == "__main__":
  sol = Solution()
  print sol.search([5,6,7,8,9,0,1,2,3,4], 5)