class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ####iteratively
        res = [[]]
        for num in nums:
            res += [i + [num] for i in res]
        return res
    
        ####recursively: DFS
        self.res = []
        self.subsetsRecu(nums, 0, [])
        return self.res
    def subsetsRecu(self, nums, index, path):
        self.res.append(path)
        for i in range(index, len(nums)):
            self.subsetsRecu(nums, i + 1, path + [nums[i]])
