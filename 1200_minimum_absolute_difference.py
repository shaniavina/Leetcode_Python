class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(arr)
        diff = float('inf')
        res = []
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] < diff:
                diff = nums[i + 1] - nums[i]
                res = [(nums[i], nums[i + 1])]
            elif nums[i + 1] - nums[i] == diff:
                res.append((nums[i], nums[i + 1]))
        return res
