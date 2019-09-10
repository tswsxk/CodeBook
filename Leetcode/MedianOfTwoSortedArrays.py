class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    m = len(nums1)
    n = len(nums2)
    temp = None
    if (m + n) % 2 == 0:
      evenTag = True
    else:
      evenTag =False
    if not nums1 or not nums2:
      temp = nums1 + nums2
    elif nums1[0] >= nums2[-1]:
      temp = nums2 + nums1
    elif nums1[-1] <= nums2[0]:
      temp = nums1 + nums2
    if temp:
      if evenTag:
        return float(temp[(m + n) // 2 - 1] +temp[(m + n) // 2]) /2
      else:
        return temp[(m + n) // 2]

    head = 0
    tail = m - 1
    cur = 0
    target_pos = (m + n) // 2
    while cur < n:
      num2 = nums2[cur]
      while head < tail - 1:
        mid = nums1[(head + tail) // 2]
        if num2 < mid:
          tail = (head + tail) // 2
        else:
          head = (head + tail) // 2
      if num2 > nums1[tail]:
        pos = tail + cur + 1
      elif num2 < nums1[head]:
        pos = head + cur
      else:
        pos = head + cur + 1
      if pos == target_pos:
        if evenTag:
          n1 = num2
          if cur == 0:
            n2 = nums1[target_pos - 1]
          elif target_pos - cur - 1 < 0 or target_pos - cur - 1 >= m:
            n2 = nums2[cur - 1]
          else:
            if nums2[cur - 1] > nums1[target_pos - cur - 1]:
              n2 = nums2[cur - 1]
            else:
              n2 = nums1[target_pos - cur - 1]
          return float(n1 + n2) / 2
        else:
          return num2
      elif pos > target_pos:
        n1 = nums1[target_pos - cur]
        if evenTag:
          if cur == 0:
            n2 = nums1[target_pos - 1]
          elif target_pos - cur - 1 < 0 or target_pos - cur - 1 >= m:
            n2 = nums2[cur - 1]
          else:
            if nums2[cur - 1] > nums1[target_pos - cur - 1]:
              n2 = nums2[cur - 1]
            else:
              n2 = nums1[target_pos - cur - 1]
          return float(n1 + n2) / 2
        else:
          return n1
      tail = m - 1
      cur += 1
    if evenTag:
      n1 = nums1[target_pos - n]
      if nums2[n - 1] > nums1[target_pos - n - 1]:
        n2 = nums2[n - 1]
      else:
        n2 = nums1[target_pos - n - 1]
      return float(n1 + n2) / 2
    else:
      return nums1[target_pos - n]
class Solution1(object):
  def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    m = len(nums1)
    n = len(nums2)
    temp = None
    if (m + n) % 2 == 0:
      evenTag = True
    else:
      evenTag = False
    if not nums1 or not nums2:
      temp = nums1 + nums2
    elif nums1[0] > nums2[-1]:
      temp = nums2 + nums1
    elif nums1[-1] < nums2[0]:
      temp = nums1 + nums2
    if temp:
      if evenTag:
        res = float(temp[(m + n) // 2 - 1] + temp[(m + n) // 2]) / 2
      else:
        res = temp[(m + n) // 2]
      return res
    cur = 0
    head = 0
    tail = m - 1
    if evenTag:
      target_pos = (m + n) // 2 - 1
      while cur < n:
        num2 = nums2[cur]
        mid = nums1[(head + tail) // 2]
        if num2 > mid:
          head = (head + tail) // 2
        else:
          tail = (head + tail) // 2
        while head < tail - 1:
          mid = nums1[(head + tail) // 2]
          if num2 > mid:
            head = (head + tail) // 2
          else:
            tail = (head + tail) // 2
        if num2 > nums1[head]:
          up = 1
          if head == m - 1:
            if target_pos - cur == head:
              n1 = nums1[head]
            else:
              n1 = nums2[target_pos - m]
            n2 = nums2[target_pos - m + 1]
            return float(n1 + n2) / 2
        else:
          up = 0
        pos = up + head + cur
        if pos == target_pos:
          n1 = num2
          if cur + 1 >= n:
            n2 = nums1[target_pos + 1 - (cur + 1)]
          else:
            if nums2[cur + 1] < nums1[target_pos + 1 - (cur + 1)]:
              n2 = nums2[cur + 1]
            else:
              n2 = nums1[target_pos + 1 - (cur + 1)]
          return float(n1 + n2) / 2
        elif pos > target_pos:
          n1 = nums1[target_pos - cur]
          if target_pos - cur + 1 >= m:
            n2 = nums2[cur]
          else:
            if cur >= n:
              n2 = nums1[target_pos - cur + 1]
            elif nums2[cur] < nums1[target_pos - cur + 1]:
              n2 = nums2[cur]
            else:
              n2 = nums1[target_pos - cur + 1]
          return float(n1 + n2) / 2
        tail = m - 1
        cur += 1
      return nums1[target_pos - n]
    else:
      target_pos = (m + n) // 2
      while cur < n:
        num2 = nums2[cur]
        mid = nums1[(head + tail) // 2]
        if num2 > mid:
          head = (head + tail) // 2
        else:
          tail = (head + tail) // 2
        while head < tail - 1:
          mid = nums1[(head + tail) // 2]
          if num2 > mid:
            head = (head + tail) // 2
          else:
            tail = (head + tail) // 2
        if num2 > nums1[head]:
          if head == m - 1:
            if target_pos - cur == head:
              return nums1[head]
            return nums2[target_pos - m]
          up = 1
        else:
          up = 0
        pos = up + head + cur
        if pos == target_pos:
          return num2
        elif pos > target_pos:
          return nums1[target_pos - cur]
        tail = m - 1
        cur += 1
      return nums1[target_pos - n]

if __name__ == "__main__":
  sol = Solution()
  testcase = [[[1, 2, 4], [3]], [[2], [1, 3, 4]], [[1, 3], [2, 4, 5]], [[1], [1]], [[2], [1, 3]], [[1, 2], [3, 4]], [[1, 2], [1, 2]], [[], [1]], [[1, 3, 5, 7], [4, 8]], [[1, 2], [3]]]
  for x in testcase:
    res = sol.findMedianSortedArrays(x[0], x[1])
    check = sorted(x[0] + x[1])
    m = len(x[0])
    n = len(x[1])
    print(x[0], x[1], res, res == float(check[(m + n - 1) // 2] + check[(m + n) // 2]) / 2)
