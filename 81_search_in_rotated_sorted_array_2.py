class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) / 2
            if nums[mid] == target:
                return True
            elif nums[l] == nums[mid]:   ###handle the duplicates
                l += 1
            elif (nums[l] <= target < nums[mid]) or (nums[l] > nums[mid] and not (nums[mid] < target <= nums[r])):
                r = mid - 1
            else:
                l = mid + 1
        return  False
    
   
