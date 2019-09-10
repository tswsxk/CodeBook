# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = 0
        check = head
        while check:
            l += 1
            check = check.next
        n = l - n
        if n == 0:
            return head.next
        count = 1
        front = head
        check = head.next
        while check:
            if count == n:
                if check.next == None:
                    front.next = None
                    return head
                else:
                    front.next = check.next
                    return head
            front = check
            check = check.next
            count += 1

def initlist(listnum):
  head = ListNode(listnum[0])
  tail = head
  for num in listnum[1:]:
    tail.next = ListNode(num)
    tail = tail.next
  return head


if __name__ == "__main__":
    sol = Solution()
    head = initlist([1,2,3,4])
    sol.removeNthFromEnd(head, 1)