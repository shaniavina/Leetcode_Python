class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(sorted(candidates), target, 0, [])
        return self.res
    def dfs(self, nums, target, index, path):
        if target < 0:
            return
        if target == 0:
            self.res.append(list(path))
        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]])
            
