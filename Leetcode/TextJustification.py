class Solution(object):
  def fullJustify(self, words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    res = []
    tmp = []
    wordlen = 0
    for word in words:
      if wordlen + len(word) + len(tmp) > maxWidth:
        if len(tmp) == 1:
          res.append(tmp[0] + " " * (maxWidth - wordlen))
          wordlen = len(word)
          tmp = [word]
        else:
          minws = (maxWidth - wordlen) // (len(tmp) - 1)
          upind = (maxWidth - wordlen) % (len(tmp) - 1) + 1
          tmpres = (" " * minws).join([(" " * (minws + 1)).join(tmp[0:upind]),(" " * minws).join(tmp[upind:])])
          res.append(tmpres)
          wordlen = len(word)
          tmp = [word]
      else:
        tmp.append(word)
        wordlen += len(word)
    if len(tmp) == 1:
      res.append(tmp[0] + " " * (maxWidth - wordlen))
    else:
      tmpres = " ".join(tmp)
      tmpres = tmpres + " " * (maxWidth - len(tmpres))
      res.append(tmpres)
    return res

if __name__ == "__main__":
  sol = Solution()
  sol.fullJustify(["This", "is", "and", "example", "of", "text", "justification."], 16)