class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max = 0
        for x in nums:
            if x == 1:
                count += 1
                if count >= max:      ### max = max(max, count)
                    max = count
            else:
                count = 0
        return max
                    
####second 
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                max_count = max(count, max_count)
            else: 
                count = 0
        return max_count
                
