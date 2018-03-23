class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        l, r = 0, len(nums) - 1
        ####have to consider about null
        if not nums:
            return res
        ###left side
        while l < r:
            mid = l + (r - l) / 2
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid
        if nums[l] != target:   ###have to get exactly the same value as target
            return res
        res[0] = l
        
        r = len(nums) - 1
        ###right side
        while l < r:
            mid = l + (r - l) / 2 + 1
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid
        res[1] = r
        return res
        
