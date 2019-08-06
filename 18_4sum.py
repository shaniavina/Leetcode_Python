class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.findNsum(nums, target, 4, [], res)
        return res
    
    def findNsum(self, nums, target, N, temp, res):
        if len(nums) < N or N < 2 or N * nums[0] > target or N * nums[-1] < target:
            return 
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append(temp + [nums[l], nums[r]])
                    
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(len(nums) - N + 1):
                if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                    self.findNsum(nums[i + 1:], target - nums[i], N - 1, temp + [nums[i]], res)
                
       
