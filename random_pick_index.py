from random import randint
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res, cnt = -1, 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                res = i if randint(1, cnt + 1) == 1 else res
                cnt += 1
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
