class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        for i in range(len(nums)):
            if nums[i] > max1:
                max3 = max2
                max2 = max1
                max1 = nums[i]
                count += 1
            elif nums[i] != max1 and nums[i] > max2:
                max3 = max2
                max2 = nums[i]
                count += 1
            elif nums[i] != max2 and nums[i] != max1 and nums[i] > max3:   ####have to be distinct
                max3 = nums[i]
                count += 1
        if count < 3:
            return max1
        else:
            return max3
        
