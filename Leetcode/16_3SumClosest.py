class Solution(object):
  def threeSumClosest(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    newNums = sorted(nums)
    nearest = 2147483647
    for ind in range(len(newNums) - 2):
      if ind > 0 and newNums[ind] == newNums[ind - 1]:
        continue
      targetNum = target - newNums[ind]
      head = ind + 1
      tail = len(newNums) - 1
      while head < tail:
        if head > ind + 1 and newNums[head] == newNums[head - 1]:
          head += 1
          continue
        res = newNums[head] + newNums[tail] - targetNum
        if res == 0:
          return target
        elif abs(res) < abs(nearest):
          nearest = res
        elif res > 0:
          tail -= 1
        else:
          head += 1
    return nearest + target
if __name__ == "__main__":
  sol = Solution()
  testcase = [[[1, 1, 1, 0], 100], [[0, 1, 1, 2, 3, 4, 1, 2], 1], [[-1, -2, 3, 4, -1, -2], -1]]
  for x in testcase:
    print sol.threeSumClosest(x[0], x[1])
