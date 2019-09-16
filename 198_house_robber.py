class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ### dp[i] = max(dp[i - 1], dp[i - 2] + num[i - 1])
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        num_i = max(nums[0], nums[1])
        num_i_1 = nums[0]
        for i in range(2, len(nums)):
            num_i_1, num_i_2 = num_i, num_i_1
            num_i = max(num_i_1, nums[i] + num_i_2)
        return num_i

    
