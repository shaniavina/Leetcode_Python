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
                    
