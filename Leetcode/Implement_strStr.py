class Solution(object):
  def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle == "":
      return 0
    for i, c in enumerate(haystack):
      if i > len(haystack) - len(needle):
        break
      findTag = True
      for j in range(len(needle)):
        if i + j >= len(haystack) or haystack[i + j] != needle[j]:
          findTag = False
          break
      if findTag:
        return i
    return -1