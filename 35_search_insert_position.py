class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if not nums:
            return 0
        
        left, right = 0, len(nums) - 1
        while left <= right:      ###if < without =, may not get in the loop when there is only one element
            mid = left + (right - left) / 2
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left
      
    
    
        
        
        
        
      
