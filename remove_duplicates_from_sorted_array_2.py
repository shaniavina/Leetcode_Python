class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        last, i, same = 0, 1, False
        while i < len(nums):
            if nums[i] != nums[last] or not same:
                same = nums[i] == nums[last]
                last += 1
                nums[last] = nums[i]
            i += 1
        return last + 1
        

        
        class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        tail = 0
        for num in nums:
            if tail < 2 or num != nums[tail - 1] or num != nums[tail - 2]:
                nums[tail] = num
                tail += 1
        return tail
