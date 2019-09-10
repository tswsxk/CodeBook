class Solution(object):
  def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    quickdict = {}
    for str in strs:
      hashvalue = 0
      hashdict = {}
      for char in str:
        if char not in hashdict:
          hashdict[char] = 1
          hashvalue += 1 << (ord(char) - ord('a'))
        else:
          hashdict[char] += 1
      if hashvalue not in quickdict:
        quickdict[hashvalue] = [(hashdict, [str])]
      else:
        findtag = False
        for item in quickdict[hashvalue]:
          tag = True
          checkdict, con = item[0], item[1]
          for c in hashdict:
            if c not in checkdict or hashdict[c] != checkdict[c]:
              tag = False
              break
          if tag:
            con.append(str)
            findtag = True
            break
        if not findtag:
          quickdict[hashvalue].append((hashdict, [str]))
    res = []
    for hv in quickdict:
      lists = quickdict[hv]
      res += [l[1] for l in lists]
    return res


if __name__ == "__main__":
  sol = Solution()
  print sol.groupAnagrams(["aa", "aaa"])