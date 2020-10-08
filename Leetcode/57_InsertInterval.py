# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
          return [newInterval]
        ind = 0
        while ind < len(intervals):
          if intervals[ind].start <= newInterval.start:
            if intervals[ind].end >= newInterval.end:
              return intervals
            elif intervals[ind].end < newInterval.start:
              ind += 1
            else: # Interval.start <= intervals[ind].end < newInterval.end
              merge_interval = intervals[ind]
              merge_interval.end = newInterval.end
              head = ind
              ind += 1
              while ind < len(intervals):
                if merge_interval.end < intervals[ind].start:
                  return intervals[:head] + [merge_interval] + intervals[ind:]
                elif merge_interval.end <= intervals[ind].end:
                  merge_interval.end = intervals[ind].end
                  ind += 1
                else:
                  ind += 1
              return intervals[:head] + [merge_interval]
          else: # newInterval.start < intervals[ind].start
            if newInterval.end < intervals[ind].start:
              return intervals[:ind] + [newInterval] + intervals[ind:]
            elif newInterval.end <= intervals[ind].end:
              intervals[ind].start = newInterval.start
              return intervals
            else:
              merge_interval = newInterval
              head = ind
              ind += 1
              while ind < len(intervals):
                if merge_interval.end < intervals[ind].start:
                  return intervals[:head] + [merge_interval] + intervals[ind:]
                elif merge_interval.end <= intervals[ind].end:
                  merge_interval.end = intervals[ind].end
                  ind += 1
                else:
                  ind += 1
              return intervals[:head] + [merge_interval]
        return intervals + [newInterval]

if __name__ == "__main__":
  lists, ilist= [[0,5],[9,12]], [7,16]
  toinsert = [Interval(s, e) for s, e in lists]
  insint = Interval(ilist[0], ilist[1])
  sol = Solution()
  sol.insert(toinsert, insint)
