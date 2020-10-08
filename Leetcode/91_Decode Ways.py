# coding: utf-8
# create by tongshiwei on 2018/4/27

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        dp = [[-1 for _ in range(3)] for _ in range(n)]
        for i in range(n):
            if i < n - 1:
                if 10 <= int(s[i: i+2]) <= 26:
                    dp[i][1] = 1
                else:
                    dp[i][1] = 0
            if int(s[i]) == 0:
                dp[i][0] = 0
            else:
                dp[i][0] = 1

        def insert_calc(idx):
            if dp[idx][-1] != -1:
                return dp[idx][-1]
            if idx == n - 1:
                if dp[idx][0] == 1:
                    return 1
                else:
                    return 0
            elif idx == n - 2:
                res = 0
                if dp[idx][1] == 1:
                    res += 1
                if dp[idx][0] == 1:
                    res += insert_calc(idx + 1)
                return res
            elif idx >= n:
                raise Exception()
            res = 0
            if dp[idx][0] == 1:
                res += insert_calc(idx + 1)
            if dp[idx][1] == 1:
                res += insert_calc(idx + 2)
            dp[idx][-1] = res
            return res
        return insert_calc(0)

if __name__ == '__main__':
    sol = Solution()
    s = "123123"
    print(sol.numDecodings(s))