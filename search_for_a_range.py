class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1
        res = [-1] * 2
        if not nums:
            return [-1, -1]
        ###left side
        while l < r:
            mid = l + (r - l) / 2
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid
        if nums[l] == target:
            res[0] = l
        else:
            return [-1, -1]
        
        l, r = 0, len(nums) - 1
        ###right side
        while l < r:
            mid = l + (r - l) / 2 + 1
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid
        if nums[r] == target:
            res[1] = r
        else:
            return [-1, -1]
        return res
        
