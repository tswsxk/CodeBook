class Solution(object):
  def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    nums.sort()

if __name__ == "__main__":
  l = [1,2,4,0]
  l.sort()
  print l