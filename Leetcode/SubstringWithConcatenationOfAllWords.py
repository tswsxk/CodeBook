class SolutionRecursive(object):
  def findSubstring(self, s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    def matchStr(index, matchWords, wordl):
      if not matchWords:
        return True
      if s[index:index + wordl] in matchWords and matchWords[s[index:index + wordl]] > 0:
        matchWords[s[index:index + wordl]] -= 1
        res = matchStr(index + wordl, matchWords, wordl)
        matchWords[s[index:index + wordl]] += 1
        return res
      return False

    tl = sum([len(x) for x in words])
    res = []
    wordl = len(words[0])
    mws = {}
    for x in words:
      if x in mws:
        mws[x] += 1
      else:
        mws[x] = 1
    for i in range(len(s) - tl + 1):
      if matchStr(i, mws, wordl):
        res.append(i)
    return res

class Solution(object):
  def findSubstring(self, s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    tl = sum([len(x) for x in words])
    res = []
    wordl = len(words[0])
    mws = {}
    for x in words:
      if x in mws:
        mws[x] += 1
      else:
        mws[x] = 1
    for i in range(len(s) - tl + 1):
      cur_dict = {}
      failTag = False
      for j in range(len(words)):
        check_word = s[i + j * wordl:i + (j + 1) * wordl]
        if check_word in mws:
          if check_word not in cur_dict:
            cur_dict[check_word] = 1
          else:
            cur_dict[check_word] += 1
          if cur_dict[check_word] > mws[check_word]:
            failTag = True
            break
        else:
          failTag = True
          break
      if not failTag:
        res.append(i)
    return res
if __name__ == "__main__":
  sol = Solution()
  print sol.findSubstring("barfoothefoobarman", ["foo","bar"])






