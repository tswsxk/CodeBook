class Solution(object):
  def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    nums = "1"
    for i in range(n - 1):
      curnum = None
      count = 0
      res = ""
      for num in str(nums):
        if num != curnum:
          if curnum is not None:
            res += (str(count) + curnum)
          curnum = num
          count = 1
        else:
          count += 1
      res += (str(count) + curnum)
      nums = res
    return nums

if __name__ == "__main__":
  sol = Solution()
  sol.countAndSay(4)
