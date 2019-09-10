class Solution(object):
  def isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    si = 0
    pi = 0
    sh = -1
    ph = -1
    while si < len(s):
      if pi < len(p) and p[pi] == "*":
        while pi < len(p) and p[pi] == "*":
          pi += 1
        sh = si
        ph = pi
      elif pi < len(p) and (s[si] == p[pi] or p[pi] == "?"):
        si += 1
        pi += 1
      elif ph > 0:
        si = sh
        sh += 1
        pi = ph
      else:
          return False
    while pi < len(p) and p[pi] == "*":
      pi += 1
    return si == len(s) and pi == len(p)

if __name__ == "__main__":
  sol = Solution()
  sol.isMatch("aaa", "*")