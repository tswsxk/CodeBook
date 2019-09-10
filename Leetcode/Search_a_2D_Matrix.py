class Solution(object):
  def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    rn_head = 0
    rn_tail = len(matrix) - 1

    while rn_head <= rn_tail:
      mid = (rn_head + rn_tail) // 2
      if matrix[mid][0] <= target <= matrix[mid][-1]:
        cn_head = 0
        cn_tail = len(matrix[mid]) - 1
        while cn_head <= cn_tail:
          cn_mid = (cn_head + cn_tail) // 2
          if matrix[mid][cn_mid] == target:
            return True
          elif matrix[mid][cn_mid] < target:
            cn_head = cn_mid + 1
          else:
            cn_tail = cn_mid - 1
        return False
      elif matrix[mid][0] > target:
        rn_tail = mid - 1
      else:
        rn_head = mid + 1
    return False

if __name__ == "__main__":
  sol = Solution()
  print sol.searchMatrix([[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 50]], 13)