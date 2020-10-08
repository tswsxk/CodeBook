# coding: utf-8
# create by tongshiwei on 2018/4/28
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return [None]


        def _generate(left, root, right):
            if len(left) == len(right) == 0:
                return [TreeNode(root)]
            if len(left) == 0:
                lnodes = [None]
            else:
                lnodes = []
                for i in range(len(left)):
                    lnodes += _generate(left[0:i], left[i], left[i+1:])
            if len(right) == 0:
                rnodes = [None]
            else:
                rnodes = []
                for i in range(len(right)):
                    rnodes += _generate(right[0:i], right[i], right[i+1:])
            root_nodes = []
            for l in lnodes:
                for r in rnodes:
                    root_node = TreeNode(root)
                    root_node.left, root_node.right = l, r
                    root_nodes.append(root_node)
            return root_nodes

        number_list = list(range(1, n + 1))
        res = []
        for i in range(n):
            res += _generate(number_list[0:i], number_list[i], number_list[i+1:])
        return res

if __name__ == '__main__':
    s = Solution()
    a = s.generateTrees(2)
    print(len(a))