class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # if max(nums) < 0:
        #     return max(nums)
        global_max, local_max = float('-inf'), 0
        for num in nums:
            local_max = max(local_max + num, num)
            global_max = max(local_max, global_max)
        return global_max
            
            
            
