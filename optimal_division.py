class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))
        if len(nums) > 2:
            nums[1] = '(' + nums[1]
            nums[-1] = nums[-1] + ')'
        return '/'.join(nums)
