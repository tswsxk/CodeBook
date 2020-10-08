class Solution(object):
  def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
      return ""
    elif len(strs) == 1:
      return strs[0]
    ls = [len(s) for s in strs]
    cp = ""
    for ind in range(min(ls)):
      check = strs[0][ind]
      for s in strs:
        if s[ind] != check:
          return cp
      cp += check
    return cp

if __name__ == "__main__":
  sol =Solution()
  testcase = [["abc", "rrrr"], ["abcac", "aaaa", "abb"], ["aabb", "aa"], ["aaa", "", "aaa"]]
  for x in testcase:
    print sol.longestCommonPrefix(x)
