# coding: utf-8
# create by tongshiwei on 2018/4/27
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        bigger_equal = head
        bigger_equal_idx = 0
        little = head
        little_idx = 0
        while bigger_equal is not None and little is not None:
            while little is not None and little.val >= x:
                little = little.next
                little_idx += 1
            while bigger_equal is not None and bigger_equal.val < x:
                bigger_equal = bigger_equal.next
                bigger_equal_idx += 1
            if little_idx > bigger_equal_idx:
                if little is None or bigger_equal is None:
                    break
                bigger_equal.val, little.val = little.val, bigger_equal.val
                little = little.next
                little_idx += 1
                bigger_equal = bigger_equal.next
                bigger_equal_idx += 1
            elif little:
                little = little.next
                little_idx += 1
            else:
                break
        return head

if __name__ == '__main__':
    a = [6,5,4,3,2,1]
    x = 3
    next = ListNode(a[-1])
    for n in reversed(a[:-1]):
        node = ListNode(n)
        next, node.next = node, next
    head = node
    s = Solution()
    s.partition(head, x)
    while head:
        print(head.val)
        head = head.next