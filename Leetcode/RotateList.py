# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # getlen
        ind = head
        l = 0
        while ind:
          l += 1
          ind = ind.next
        if l == 0:
          return head
        k %= l
        if k == 0:
          return head
        leftpos = l - k
        count = 1
        ind = head.next
        forehead = head
        while count < leftpos:
          count += 1
          forehead = ind
          ind = ind.next
        new_head = ind
        forehead.next = None
        while ind.next is not None:
          ind = ind.next
        ind.next = head
        return new_head
