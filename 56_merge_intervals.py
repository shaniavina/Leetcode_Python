class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key = lambda x: x[0])
        res = [intervals[0]]
        for n in intervals[1:]:
            if res[-1][1] >= n[0]:
                res[-1][1] = max(res[-1][1], n[1])
            else:
                res.append(n)
        return res
