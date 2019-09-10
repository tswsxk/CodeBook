class Solution(object):
  def trap(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    if len(height) <= 2:
      return 0
    left = 0
    right = len(height) - 1
    h = min([height[right], height[left]])
    area = h * (right - left - 1)
    lhest = height[left]
    rhest = height[right]
    while True:
      if height[left] <= height[right]:
        left += 1
        if left >= right:
          break
        area -= min([h, height[left]])
        if height[left] > lhest:
          area += (min([height[left], height[right]]) - h) * (right - left - 1)
          h = min([height[left], height[right]])
          lhest = height[left]
      else:
        right -= 1
        if right <= left:
          break
        area -= min([h, height[right]])
        if height[right] > rhest:
          area += (min([height[left], height[right]]) - h) * (right - left - 1)
          h = min([height[left], height[right]])
          rhest = height[right]

    return area

if __name__ == "__main__":
  sol = Solution()
  print sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])

