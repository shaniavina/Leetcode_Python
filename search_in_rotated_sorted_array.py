class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            
            if nums[mid] == target:
                return mid
            elif (nums[left] <= nums[mid] and nums[left] <= target < nums[mid]) or (nums[left] > nums[mid] and not (nums[mid] < target <= nums[right])):
                right = mid - 1
            else:
                left = mid + 1
        return -1
