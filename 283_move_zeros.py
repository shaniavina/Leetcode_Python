class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # two pointers
        pos = 0 
        for i in range(len(nums)):
            if nums[i]:
                nums[pos],nums[i] = nums[i],nums[pos]
                pos += 1

                
