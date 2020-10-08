class Solution(object):
  def largestRectangleArea(self, heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    if len(heights) is 0:
      return 0
    record = [[None] * (len(heights) - i) for i in range(len(heights))]
    minnum = [[None] * (len(heights) - i) for i in range(len(heights))]
    for i in range(len(heights)):
      record[i][0] = minnum[i][0] = heights[i]
    def largestRectangleAreaRecursive(left, right):
      '''
      include right
      :param left:
      :param right:
      :return:
      '''
      assert right >= left
      if right > left:
        if record[left][right-left] is not None:
          assert minnum[left][right - left] is not None
          return record[left][right - left], minnum[left][right - left]
        left_part_marea, left_part_min = largestRectangleAreaRecursive(left, right - 1)
        right_part_marea, right_part_min = largestRectangleAreaRecursive(left + 1, right)
        minnum[left][right - left] = min(left_part_min, right_part_min)
        record[left][right - left] = max(left_part_marea, right_part_marea,
                                  minnum[left][right - left] * (right - left + 1))
      return record[left][right-left], minnum[left][right-left]

    max_area, _ = largestRectangleAreaRecursive(0, len(heights) - 1)
    return max_area

if __name__ == "__main__":
  sol = Solution()
  print sol.largestRectangleArea([2,1,5,6,2,3])
