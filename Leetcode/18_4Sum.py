class Solution(object):
  def fourSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    newnums = sorted(nums)
    res = []
    for ind1 in range(len(newnums) - 3):
      if ind1 > 0 and newnums[ind1] == newnums[ind1 - 1]:
        continue
      for ind2 in range(ind1 + 1, len(newnums) - 2):
        if ind2 > ind1 + 1 and newnums[ind2] == newnums[ind2 - 1]:
          continue
        head = ind2 + 1
        tail = len(newnums) - 1
        targetNum = target - newnums[ind1] - newnums[ind2]
        while head < tail:
          if head > ind2 + 1 and newnums[head] == newnums[head - 1]:
            head += 1
            continue
          if tail < len(newnums) - 2 and newnums[tail] == newnums[tail + 1]:
            tail -= 1
            continue
          if newnums[head] + newnums[tail] == targetNum:
            res.append([newnums[ind1], newnums[ind2], newnums[head], newnums[tail]])
            head += 1
            tail -= 1
          elif newnums[head] + newnums[tail] < targetNum:
            head += 1
          else:
            tail -= 1
    return res

if __name__ == "__main__":
  sol = Solution()
  testcase = [[[1, 0, -1, 0, -2, 2], 0], [[1, 1, 1, 1, 1], 4], [[1, -1, -1, 1, 2, -1, 3], 0]]
  for x in testcase:
    print sol.fourSum(x[0], x[1])
