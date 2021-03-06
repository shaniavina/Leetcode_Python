# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        i = 0
        while i < len(intervals) and newInterval.start > intervals[i].end:
            res.append(intervals[i])
            i += 1
        while i < len(intervals) and newInterval.end >= intervals[i].start:
            newInterval = Interval(min(newInterval.start, intervals[i].start), max(newInterval.end, intervals[i].end))
            i += 1
        res.append(newInterval)
        res += intervals[i:]
        return res
