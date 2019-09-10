class Solution(object):
  def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) <= 1:
      return s
    res = s[0]
    for head in range(1, len(s)):
      if s[head] == s[head - 1]:
        ind = 1
        while ind <= head - 1 and head + ind < len(s):
          if s[head - 1 - ind] != s[head + ind]:
            break
          ind += 1
        if len(res) < len(s[head - 1 - (ind - 1):head + ind]):
          res = s[head - 1 - (ind - 1):head + ind]
      if head > 1 and s[head] == s[head - 2]:
        ind = 1
        mid = head - 1
        while ind <= mid and mid + ind < len(s):
          if s[mid - ind] != s[mid + ind]:
            break
          ind += 1
        if len(res) < len(s[mid - (ind - 1):mid + ind]):
          res = s[mid - (ind - 1):mid + ind]
    return res


if __name__ == "__main__":
  sol = Solution()
  testcase = ["aaaa", "cabal", "a", "", "abba", "abcabba", "aba", "acaabbabcb", "sfjdlajflaskjflkajkfljaljvf"]
  for x in testcase:
    print sol.longestPalindrome(x)