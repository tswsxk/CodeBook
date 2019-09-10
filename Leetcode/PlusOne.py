class Solution(object):
  def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    up = 1
    ind = len(digits) - 1
    while up == 1 and ind >= 0:
      digits[ind] += up
      up = digits[ind] // 10
      digits[ind] %= 10
      ind -= 1
    if up == 1:
      return [1] + digits
    else:
      return digits

if __name__ == "__main__":
  sol = Solution()
  sol.plusOne([2,9,9])