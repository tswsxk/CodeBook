class Solution(object):
  def nextPermutation(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if len(nums) <= 1:
      return
    ind = len(nums) - 1
    breaktag = False
    while ind > 0:
      if nums[ind - 1] > nums[ind]:
        breaktag = True
      elif breaktag and nums[ind - 1] < nums[ind]:
        break
      elif nums[ind - 1] < nums[ind]:
        temp = nums[ind - 1]
        nums[ind - 1] = nums[ind]
        nums[ind] = temp
        return
      ind -= 1
    if ind == 0:
      nums.reverse()
      return
    cmpnum = nums[ind - 1]
    for idx in range(len(nums) - 1, ind - 1, -1):
      if cmpnum < nums[idx]:
        temp = nums[idx]
        nums[idx] = cmpnum
        nums[ind - 1] = temp
        break
    for idx in range(0, (len(nums) - ind + 1) // 2):
      temp = nums[ind + idx]
      nums[ind + idx] = nums[len(nums) - 1 - idx]
      nums[len(nums) - 1 -idx] = temp

if __name__ == "__main__":
  sol = Solution()
  testcase = [
    # [],
    # [1],
    # [3, 2, 1],
    # [1, 2, 3],
    # [3, 1, 2],
    # [2, 1, 3],
    [1, 2, 5, 4, 2, 1],
    [1, 3, 9, 10, 34, 6, 7, 7],
    [1, 1, 1, 2, 2, 2, 3, 3, 3]
  ]
  for x in testcase:
    sol.nextPermutation(x)
    print x
