class Solution(object):
  def generateMatrix(self, n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    count = 1
    ret = [[0 for _ in range(n)] for _ in range(n)]
    upbound, downbound, leftbound, rightbound = 0, n - 1, 0, n - 1
    while count <=  n * n:
      # right move
      new_count = count + (rightbound - leftbound) + 1
      count, ret[upbound][leftbound: rightbound + 1] = new_count, range(count, new_count)
      if count > n * n:
        break
      upbound += 1

      # down move
      new_count = count + (downbound - upbound) + 1
      count, new_ret = new_count, range(count, new_count)
      for i, row in enumerate(ret[upbound: downbound + 1]):
        row[rightbound] = new_ret[i]
      if count > n * n:
        break
      rightbound -= 1

      # left move
      new_count = count + (rightbound - leftbound) + 1
      count, ret[downbound][leftbound: rightbound + 1] = new_count, range(new_count - 1, count - 1, -1)
      if count > n * n:
        break
      downbound -= 1

      # up move
      new_count = count + (downbound - upbound) + 1
      count, new_ret = new_count, range(new_count - 1, count - 1, -1)
      for i, row in enumerate(ret[upbound: downbound + 1]):
        row[leftbound] = new_ret[i]
      if count > n * n:
        break
      leftbound += 1
    return ret

if __name__ == "__main__":
  sol = Solution()
  sol.generateMatrix(2)



