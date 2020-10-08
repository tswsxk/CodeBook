#!/usr/bin/python

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        tree_num_table = [-1 for _ in range(n + 1)]
        tree_num_table[0] = 1
        tree_num_table[1] = 1

        def _num_trees(num):
            if tree_num_table[num] != -1:
                return tree_num_table[num]
            else:
                res = 0
                for i in range(num):
                    res += _num_trees(i) * _num_trees(num - i - 1)
                tree_num_table[num] = res
                return res
        return _num_trees(n)

if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(4))