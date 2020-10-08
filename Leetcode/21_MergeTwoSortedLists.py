# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
  def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1 and not l2:
      return l1
    elif not l1:
      return l2
    elif not l2:
      return l1
    if l2.val > l1.val:
      newl = ListNode(l1.val)
      l1 = l1.next
    else:
      newl = ListNode(l2.val)
      l2 = l2.next
    head = newl
    while l2 and l1:
      if l2.val < l1.val:
        newNode = ListNode(l2.val)
        newl.next = newNode
        newl = newNode
        l2 = l2.next
      else:
        newNode = ListNode(l1.val)
        newl.next = newNode
        newl = newNode
        l1 = l1.next
    if l1:
      newl.next = l1
    if l2:
      newl.next = l2
    return head