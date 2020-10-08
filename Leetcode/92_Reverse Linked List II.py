# coding: utf-8
# create by tongshiwei on 2018/4/28

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        idx = 1
        if m > 1:
            brhead = head
            while idx < m - 1:
                idx += 1
                brhead = brhead.next
            rhead = brhead.next
            idx += 1
        else:
            brhead = None
            rhead = head
        fp = rhead
        lp = rhead.next
        while idx < n:
            idx += 1
            next_lp = lp.next
            lp.next = fp
            fp = lp
            lp = next_lp
        rhead.next = lp
        if brhead is not None:
            brhead.next = fp
        else:
            head = fp
        return head
if __name__ == '__main__':
    s = Solution()
    a = [1, 2, 3, 4, 5, 6, 7]
    next = ListNode(a[-1])
    for n in reversed(a[:-1]):
        node = ListNode(n)
        next, node.next = node, next
    head = node
    head = s.reverseBetween(head, 1, 7)
    while head:
        print(head.val)
        head = head.next





