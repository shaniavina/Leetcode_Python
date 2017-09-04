class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#         ####recursively: DFS
#         self.res = []
#         self.subsetsRecu(sorted(nums), 0, [])    
#         return self.res
#     def subsetsRecu(self, nums, index, path):
#         self.res.append(path)
#         for i in range(index, len(nums)):            
#             if i > index and nums[i] == nums[i - 1]:  ####handle duplicate: 1. sort; 2. discuss when nums[i] == nums[i-1]
#                 continue
#             else:
#                 self.subsetsRecu(nums, i + 1, path + [nums[i]])
            
            
             ####iteratively
        res = [[]]
        nums.sort()
        for num in nums:
            res += [i + [num] for i in res if i + [num] not in res]    ###check if it exists
        return res
