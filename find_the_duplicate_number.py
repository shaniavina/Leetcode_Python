class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums) - 1

        while left <= right:
            mid = left + (right - left) / 2
            
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                right = mid - 1 
            else:
                left = mid + 1
        return left
