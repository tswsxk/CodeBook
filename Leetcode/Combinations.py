class Solution(object):
  def combine(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    res = []
    def find_combine(d, array, tmpres):
      if d == k:
        res.append(tmpres)
      for i, num in enumerate(array):
        if len(array) - i < k - d:
          break
        else:
          find_combine(d + 1, array[i + 1:], tmpres + [num])
    find_combine(0, list(range(1, n + 1)), [])
    return res

if __name__ == "__main__":
  sol = Solution()
  sol.combine(3, 2)