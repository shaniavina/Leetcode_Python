class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            if 3 * nums[i] >= target:   ####lower bound
                return res
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]   
                if s < target:
                    res += r - l    ###you can add the whole length
                    l += 1
                else:
                    r -= 1
        return res
