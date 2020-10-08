# coding: utf-8
# create by tongshiwei on 2018/4/27

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_rec = {}
        for n in nums:
            if n not in num_rec:
                num_rec[n] = 0
            num_rec[n] += 1
        num_times = list(num_rec.items())
        end = len(num_times)

        def get_res(final_res, res, pointer):
            if pointer == end:
                final_res += [res]
                return
            val, times = num_times[pointer]
            for i in range(1, times + 1):
                get_res(final_res, res + [val] * i, pointer + 1)
            get_res(final_res, res, pointer + 1)

        final_res = []
        get_res(final_res, [], 0)
        return final_res

if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2]))


