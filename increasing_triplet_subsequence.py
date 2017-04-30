class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min, a, b = float('inf'), float('inf'), float('inf')
        for c in nums:
            if min >= c:
                min = c
            elif b >= c:
                a, b = min, c
            else:
                return True
        return False
