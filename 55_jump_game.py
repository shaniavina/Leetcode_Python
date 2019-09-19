class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        last = n - 1
        for i in reversed(range(n - 1)):
            if i + nums[i] >= last:
                last = i
        return last == 0
    
  
