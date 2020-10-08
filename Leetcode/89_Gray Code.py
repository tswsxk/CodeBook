# coding: utf-8
# create by tongshiwei on 2018/4/27
class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        order_n = [0 for _ in range(n + 1)]
        def branch(res, pre, level, next_bit):
            pre += str(next_bit)
            if level == n:
                res.append(int(pre, 2))
                return
            if order_n[level] == 0:
                branch(res, pre, level + 1, 0)
                branch(res, pre, level + 1, 1)
                order_n[level] = 1
            else:
                branch(res, pre, level + 1, 1)
                branch(res, pre, level + 1, 0)
                order_n[level] = 0
        res = []
        branch(res, '0b', 1, 0)
        branch(res, '0b', 1, 1)
        order_n[1] = 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.grayCode(0))

