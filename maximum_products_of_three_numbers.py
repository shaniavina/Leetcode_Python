class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        if max(nums) <= 0 or min(nums) >= 0 or abs(sorted_nums[0]) <= sorted_nums[-3]:
            return sorted_nums[-1] * sorted_nums[-2] * sorted_nums[-3]
        else:
            return max(sorted_nums[0] * sorted_nums[1] * sorted_nums[-1], sorted_nums[-1] * sorted_nums[-2] * sorted_nums[-3])
                
