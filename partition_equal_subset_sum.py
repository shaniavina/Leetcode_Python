class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ####same as partition into k groups
        total = sum(nums)
        k = 2
        if total % k or total / k < max(nums):
            return False
        
        nums.sort(reverse = True)
        self.subset_sums = [0] * k
        return self.dfs(nums, total / k, 0)
    def dfs(self, nums, target, i):
        if i == len(nums):
            return True
        for k in range(len(self.subset_sums)):
            if self.subset_sums[k] + nums[i] > target:
                continue
            self.subset_sums[k] += nums[i]
            if self.dfs(nums, target, i + 1):
                return True
            self.subset_sums[k] -= nums[i]
            if not self.subset_sums[k]:
                return False    
