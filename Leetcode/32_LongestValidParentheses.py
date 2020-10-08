class Solution(object):
  def longestValidParentheses(self, s):
    """
    :type s: str
    :rtype: int
    """
    head = 0
    max_length = 0
    ind = 0
    braStack = 0
    length = 0
    while ind < len(s):
      if s[ind] == "(":
        braStack += 1
      elif s[ind] == ")":
        if braStack == 0:
          max_length = max([length, max_length])
          length = 0
        elif braStack > 0:
          braStack -= 1
          length += 2
          if braStack == 0:
            max_length = max([length, max_length])
      ind += 1

    ind = len(s) - 1
    braStack = 0
    length = 0
    while ind >= 0:
      if s[ind] == ")":
        braStack += 1
      elif s[ind] == "(":
        if braStack == 0:
          max_length = max([length, max_length])
          length = 0
        elif braStack > 0:
          braStack -= 1
          length += 2
          if braStack == 0:
            max_length = max([length, max_length])
      ind -= 1

    return max_length


if __name__ == "__main__":
  sol =Solution()
  print sol.longestValidParentheses(
    "((()))())"
  )