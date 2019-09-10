class Solution(object):
  def getPermutation(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    if n == 1:
      return "1"
    tmp = 1
    factorial = [0] * n
    for i in range(n):
      factorial[i] = tmp
      tmp *= (i + 2)
    factorial = list(reversed(factorial[1:]))
    rec = [0] * (n - 1)
    k -= 1
    for i in range(1, n - 1):
      if k >= factorial[i]:
        rec[i - 1] = k // factorial[i]
        k %= factorial[i]
    rec[-1] = k
    def buildres(count, array, res):
      if count == n - 1:
        return res + str(array[0] + 1)
      else:
        num = rec[count]
        return buildres(count + 1, array[:num] + array[num + 1:], res + str(array[num] + 1))
    return buildres(0, range(n), "")

if __name__ == "__main__":
  sol = Solution()
  print sol.getPermutation(5, 1)

