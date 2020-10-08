# coding: utf-8
# create by tongshiwei on 2018/4/28

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        stack = [[root, 0]]
        while stack:
            node, tag = stack.pop()
            if tag == 0:
                stack.append([node, 1])
                if node.left is not None:
                    stack.append([node.left, 0])
            else:
                res.append(node.val)
                if node.right is not None:
                    stack.append([node.right, 0])
        return res