class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        for i in range(len(nums)):
            size = len(res)
            for j in range(size):
                res.append(list(res[j]))
                res[-1].append(nums[i])     ####add on a new element to every previous subset
        return res
