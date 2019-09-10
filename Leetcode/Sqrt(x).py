class Solution(object):
  def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    head, tail = 0, x / 2 + 1
    while head <= tail:
      mid = (head + tail) >> 1
      if mid ** 2 > x:
        tail = mid - 1
      else:
        head = mid + 1
    return tail