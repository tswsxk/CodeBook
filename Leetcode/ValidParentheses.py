class Solution(object):
  def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    leftPar = {"(": 0, "[": 1, "{": 2}
    rightPar = {")": 0, "]": 1, "}": 2}
    parStack = []
    for c in s:
      if c in leftPar:
        parStack.append(c)
      elif c in rightPar:
        if not parStack:
          return False
        if leftPar[parStack.pop()] != rightPar[c]:
          return False
      else:
        return False
    if parStack:
      return False
    return True