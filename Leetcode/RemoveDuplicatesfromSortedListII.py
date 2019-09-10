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
        check = head
        forehead = head
        forenum = None
        curnum = None
        while check:
          if curnum is None:
            curnum = check.val
          elif check.val == curnum:
            if forenum is not None:
              forenum.next = check.next
              forehead = forenum
            else:
              head = check.next
              forehead = None
          else:
            # check.val != curnum
            curnum = check.val
            forenum = forehead
            forehead = check
          check = check.next
        return head
if __name__ == "__main__":
  sol = Solution()
  sol.deleteDuplicates([1,2,3,3,4,4,5])