class Solution(object):
  def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    if len(height) == 1:
      return 0
    head = 0
    tail = len(height) - 1
    left = 0
    right = tail
    while left < right:
      if height[head] == min([height[head], height[tail]]):
        while height[left] <= height[head] and left < right:
          left += 1
        while right > left:
          if min([height[left], height[right]]) * (right - left) > height[head] * (tail - head):
            head = left
            tail = right
            break
          right -= 1
      else:
        while height[right] <= height[tail] and right > left:
          right -= 1
        while left < right:
          if min([height[left], height[right]]) * (right - left) > height[tail] * (tail - head):
            head = left
            tail = right
            break
          left += 1
    return min([height[head], height[tail]]) * (tail - head)






if __name__ == "__main__":
  sol = Solution()
  testcase = [[1, 2, 4, 3], [1, 1], [1], [3, 4, 4, 3], [4, 2, 3, 2, 1, 3]]
  for x in testcase:
    print sol.maxArea(x)
