class Solution(object):
  def lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: int
    """
    l = 0
    lastl = 0
    for c in s:
      if c == " ":
        if l > 0:
          lastl = l
        l = 0
      elif c.isalpha():
        l += 1
    if l > 0:
      lastl = l
    return lastl
