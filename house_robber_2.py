class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.robrange(nums, 0, len(nums) - 1), self.robrange(nums, 1, len(nums)))
        
    def robrange(self, nums, start, end):
        num_i, num_i_1 = nums[start], 0
        for i in range(start + 1, end):
            num_i_1, num_i_2 = num_i, num_i_1
            num_i = max(nums[i] + num_i_2, num_i_1)
        return num_i
