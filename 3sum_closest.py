class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]   ###sum() can only include two items
                if s == target:
                    return s
                if abs(res - target) > abs(s - target):
                    res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
        return res
