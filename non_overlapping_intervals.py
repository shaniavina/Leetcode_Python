# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key = lambda x:x.start)
        result, pre = 0, 0
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[pre].end:
                if intervals[i].end < intervals[pre].end:
                    pre = i
                result += 1
            else:
                pre = i
        return result
