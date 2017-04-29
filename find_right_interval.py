# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        sorted_intervals = sorted((e.start, i) for i, e in enumerate(intervals))   ####pay attention to the definition
        res = []
        for e in intervals:
            r = bisect.bisect_left(sorted_intervals, (e.end,))  ####s is with the same form as array
            res.append(sorted_intervals[r][1] if r < len(sorted_intervals) else -1)
        return res
        
