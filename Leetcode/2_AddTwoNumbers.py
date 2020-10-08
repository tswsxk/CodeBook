# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def initlist(listnum):
  head = ListNode(listnum[0])
  tail = head
  for num in listnum[1:]:
    tail.next = ListNode(num)
    tail = tail.next
  return head
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = []
        up = 0
        while l1 and l2:
          l = l1.val + l2.val + up
          up = l // 10
          re = l % 10
          res.append(re)
          l1 = l1.next
          l2 = l2.next
        while l1:
          l = l1.val +  up
          up = l // 10
          re = l % 10
          res.append(re)
          l1 = l1.next
        while l2:
          l = l2.val + up
          up = l // 10
          re = l % 10
          res.append(re)
          l2 = l2.next
        if not l1 and not l2 and up != 0:
          res.append(up)
        result = initlist(res)
        return result

if __name__ == "__main__":
  def listprint(listhead):
    listnode = listhead
    while listnode:
      if listnode != listhead:
        print("->", end="")
      print(listnode.val, end="")
      listnode = listnode.next
    print()
  l1 = initlist([5])
  l2 = initlist([5])
  sol =Solution()
  l3 = sol.addTwoNumbers(l1, l2)
  listprint(l1)
  listprint(l2)
  listprint(l3)
