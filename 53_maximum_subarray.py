class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dynamic programming
        # time: O(n)
        # space: O(1)
        if not nums:
            return 0
        global_max, local_max = float('-inf'), 0
        for num in nums:
            local_max = max(local_max + num, num)
            global_max = max(global_max, local_max)
        return global_max
    
