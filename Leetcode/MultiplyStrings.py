class Solution(object):
  def multiply(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    def add(num1, num2, offset=0):
      # return num1 + num2 << offset
      num = num1[:offset]
      ind = 0
      up = 0
      while ind + offset < len(num1) and ind < len(num2):
        tempsum = int(num1[ind + offset]) + int(num2[ind]) + up
        num += str(tempsum % 10)
        up = tempsum / 10
        ind += 1
      for digit in num1[ind+offset:]:
        tempsum = int(digit) + up
        num += str(tempsum % 10)
        up = tempsum / 10
      for digit in num2[ind:]:
        tempsum = int(digit) + up
        num += str(tempsum % 10)
        up = tempsum / 10
      if up != 0:
        num += str(up)
      return num

    def submul(num1, digit):
      # return num1 * digit
      digit = int(digit)
      if digit == 0:
        return "0"
      elif digit == 1:
        return num1
      up = 0
      res = ""
      for num in num1:
        tempres = int(num) * digit + up
        res += str(tempres % 10)
        up = tempres / 10
      if up != 0:
        res += str(up)
      return res

    if len(num1) == 1:
      if int(num1) == 0:
        return "0"
      elif int(num1) == 1:
        return num2
    num1 = num1[::-1]
    num2 = num2[::-1]
    res = "0"
    for i, digit in enumerate(num2):
      res = add(res, submul(num1, digit), i)

    return res[::-1]



