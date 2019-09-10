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
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        newl = None
        head = None
        def getListItem(ln):
          if ln:
            return ln.val
          else:
            return None
        if len(lists) == 0:
          return None
        lheads = [(x, getListItem(x)) for x in lists if x]
        lheads = sorted(lheads, key=lambda ii: ii[1])

        while True:
          if len(lheads) > 0 and lheads[0][0]:
           minN = lheads[0][1]
           arr = lheads[0][0].next
           if arr:
             newHead = (arr, getListItem(arr))
             pos = 1
             while pos < len(lheads) and newHead[1] > lheads[pos][1]:
               pos += 1
             lheads = lheads[1:pos] + [newHead] + lheads[pos:]
           else:
             lheads = lheads[1:]
          else:
            break
          if newl:
            newNode = ListNode(minN)
            newl.next = newNode
            newl = newNode
          else:
            newl = ListNode(minN)
            head = newl
        return head

if __name__ == "__main__":
  sol = Solution()
  testcase = [[1,2,3],[2,3,4],[1]]
  l = [initlist(x) for x in testcase]
  sol.mergeKLists(l)


