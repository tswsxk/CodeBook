class Solution(object):
  def isNumber(self, s):
    """
    :type s: str
    :rtype: bool
    """
    import re
    p = re.compile("(\-|\+)?(((\d)+(\.(\d)*)?)|(\.(\d)+))(e(\-|\+)?(\d)+)?")
    match = p.search(s.strip())
    if match:
      if len(match.group()) == len(s.strip()):
        return True
    return False

if __name__ == "__main__":
  sol = Solution()
  sol.isNumber("3e-2")