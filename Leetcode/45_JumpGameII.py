class Solution(object):
  def jump(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    head, tail, step = 0, 1, 0
    while head < tail and tail < len(nums):
      head, tail = tail, max([i + head + num for i, num in enumerate(nums[head:tail])]) + 1
      step += 1
    return step

# class Solution(object):
#   def jump(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     path = []
#     route = []
#
#     for i, num in enumerate(nums):
#       path.append([0])
#       route.append([i])
#       for j in range(i):
#         if j + nums[j] >= i:
#           path[j].append(1)
#           route[j].append(j)
#         else:
#           path[j].append(-1)
#           route[j].append(-1)
#       j = 0
#       if path[j][-1] == -1:
#         minpath = float('inf')
#         temproute = None
#         for ret, arr in enumerate(path[j:i]):
#           n = arr[-1]
#           if n > 0 and n + path[j][ret] < minpath:
#             minpath = n + path[j][ret]
#             temproute = j + ret
#         if temproute is not None:
#           path[j][-1] = minpath
#           route[j][-1] = temproute
#     return path[0][-1]

if __name__ == "__main__":
  sol = Solution()
  print sol.jump([2,3,1,1,4])