# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        nodeRec = []
        check = head
        precheck = head
        count = 0
        n = k
        while check:
          nodeRec.append(check)
          count += 1
          if count == n:
            count = 0
            check = check.next
            for i, x in enumerate(nodeRec):
              if i > 0:
                x.next = nodeRec[i - 1]
              else:
                x.next = check
            if nodeRec[0] == head:
              head = nodeRec[n - 1]
            else:
              precheck.next = nodeRec[n - 1]
              precheck = nodeRec[0]
            nodeRec = []
            continue
          check = check.next
        return head