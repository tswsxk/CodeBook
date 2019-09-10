class Solution(object):
  def isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    import re
    pat = re.compile(p)
    allm = pat.findall(s)
    if allm:
      if len(allm[0]) == len(s):
        return True
    return False
if __name__ == "__main__":
  sol = Solution()
  testcase = [[["aa"], ["a*"]], [["aa"], ["a"]], [["aa"], ["aa"]], [["aaa"], ["aa"]], [["aa"], [".*"]],
              [["ab"], [".*"]], [["aab"], ["c*a*b"]]]
  for x in testcase:
    print sol.isMatch("".join(x[0]), "".join(x[1]))