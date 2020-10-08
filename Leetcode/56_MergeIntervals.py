# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
          return intervals
        intervals.sort(key=lambda x: x.start)
        ind = 1
        new_intervals = [intervals[0]]
        while ind < len(intervals):
          if new_intervals[-1].end >= intervals[ind].start:
            new_intervals[-1].end = max([intervals[ind].end, new_intervals[-1].end])
          else:
            new_intervals.append(intervals[ind])
          ind += 1
        return new_intervals

if __name__ == "__main__":
  lists = [[1,3],[2,6],[8,10],[15,18]]
  sol = Solution()
  sol.merge([Interval(s, e) for s, e in lists])
