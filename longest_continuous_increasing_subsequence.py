class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res, cnt = 1, 1   ###if not null, at least you got 1
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                cnt = 1
            else:
                cnt += 1
                res = max(res, cnt)
        return res
