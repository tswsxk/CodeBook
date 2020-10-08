# coding: utf-8
# create by tongshiwei on 2018/4/20

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        max_area = 0
        for i in range(len(heights)):
            l = len(heights)
            for j in range(i, len(heights)):
                if heights[i] > heights[j]:
                    l = j
                    break
            l -= i
            area = l * heights[i]
            if max_area < area:
                max_area = area
        return max_area


if __name__ == '__main__':
    heights = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4]
    c = Solution()
    print(c.largestRectangleArea(heights))
