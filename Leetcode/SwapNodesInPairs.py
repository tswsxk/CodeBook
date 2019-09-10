# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodeRec = []
        check = head
        precheck = head
        count = 0
        n = 2
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

def initlist(listnum):
  head = ListNode(listnum[0])
  tail = head
  for num in listnum[1:]:
    tail.next = ListNode(num)
    tail = tail.next
  return head

if __name__ == "__main__":
  sol = Solution()
  sol.swapPairs(initlist([1,2,3,4]))