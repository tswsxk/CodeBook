# Longest Substring Without Repeating Characters
class Solution(object):
  def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    head = 0
    l = len(s)
    if l == 0:
      return 0
    ll = 1
    while head < l - 1:
      tail = head + 1
      record = set(s[head])
      while tail < l:
        if s[tail] in record:
          break
        else:
          record.add(s[tail])
          tail += 1
      if len(record) > ll:
        ll = len(record)
      head += 1
    return ll

if __name__ == "__main__":
  sol = Solution()
  testcase = ["au","abcabcbb"]
  for x in testcase:
    l= sol.lengthOfLongestSubstring(x)
    print(l)
