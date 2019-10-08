class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hashset// boundary point
        res, lookup = 0, {}
        for n in nums:
            if n not in lookup:
                left = lookup.get(n - 1, 0)
                right = lookup.get(n + 1, 0)
                lenth = left + right + 1
                lookup[n] = lenth
                res = max(res, lenth)
                lookup[n - left] = lenth
                lookup[n + right] = lenth
        return res
