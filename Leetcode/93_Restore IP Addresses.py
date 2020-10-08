# coding: utf-8
# create by tongshiwei on 2018/4/28

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def insert_check(pre, idx):
            res = []
            if len(pre) == 4 and idx == len(s):
                return [".".join(pre)]
            if (4 - len(pre)) * 3 < len(s[idx:]):
                return res
            for i in range(1, 4):
                if idx + i > len(s):
                    break
                subip = s[idx: idx + i]
                if len(str(int(subip))) != len(subip):
                    continue
                elif 0 <= int(subip) <= 255:
                    res += insert_check(pre + [subip], idx + i)
            return res

        return insert_check([], 0)

if __name__ == '__main__':
    s =Solution()
    print(s.restoreIpAddresses("25525511135"))
