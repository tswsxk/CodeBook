class Solution(object):
  def addBinary(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    if len(a) >= len(b):
      n1 = list(a[::-1])
      n2 = list(b[::-1])
    else:
      n1 = list(b[::-1])
      n2 = list(a[::-1])

    n1 = [int(num) for num in n1]
    n2 = [int(num) for num in n2]
    ind = 0
    up = 0
    while ind < len(n2):
      n1[ind] = n1[ind] + n2[ind] + up
      up = n1[ind] // 2
      n1[ind] %= 2
      ind += 1
    while up == 1 and ind < len(n1):
      n1[ind] += up
      up = n1[ind] // 2
      n1[ind] %= 2
      ind += 1
    if up == 1:
      return "".join(["1"] + [str(num) for num in reversed(n1)])
    else:
      return "".join([str(num) for num in reversed(n1)])

if __name__ == "__main__":
  sol = Solution()
  sol.addBinary("101", "1")