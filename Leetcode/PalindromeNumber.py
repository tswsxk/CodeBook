class Solution(object):
  def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    s = str(x)
    l = len(s)
    left = l // 2
    right = (l - 1) // 2
    for ind in range(0, left+1):
      if s[left - ind] != s[right + ind]:
        return False
    return True

if __name__ == "__main__":
  sol = Solution()
  testcase = [1234, 12321, 1, 121, 12345654321, 123321]
  for x in testcase:
    print sol.isPalindrome(x)
