class Solution(object):
  def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    if n == 0:
      return [""]
    res = []
    def genBraket(left, right, rs):
      if right == n:
        res.append(rs)
        return
      if right < left:
        genBraket(left, right + 1, rs + ")")
      if left < n:
        genBraket(left + 1, right, rs + "(")
    genBraket(1, 0, "(")
    return res

