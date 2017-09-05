class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """                   
        self.res = []
        self.dfs(sorted(candidates), 0, [], target)
        return self.res

    def dfs(self, nums, index, path, target):
        if target < 0:
            return
        if target == 0:
            self.res.append(list(path))
            
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue

            self.dfs(nums, i + 1, path + [nums[i]], target - nums[i])
