# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
          return head
        check = head.next
        forehead = head
        curnum = head.val
        while check:
          if check.val == curnum:
            forehead.next = check.next
          else:
            forehead = check
            curnum = check.val
          check = check.next
        return head

