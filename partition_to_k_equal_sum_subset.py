
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
          # Time:  O(n*2^n)
# Space: O(2^n)

        total = sum(nums)
        if total % k or total / k < max(nums):
            return False
        self.lookup = [None] * (2 ** (len(nums)))
        self.lookup[-1] = True
        return self.dfs(nums, total / k, 0, total)
    def dfs(self, nums, target, used, todo):
        if self.lookup[used] is None:
            targ = (todo - 1) % target + 1
            self.lookup[used] = any(self.dfs(nums, target, used | (1<<i), todo-num) \
                                   for i, num in enumerate(nums) if ((used>>i) & 1) == 0 and num <= targ)
        return self.lookup[used]
        
        
#### Time:  O(k^(n-k) * k!)
# # Space: O(n)
# # DFS solution with pruning.
#         total = sum(nums)
#         if total % k or total / k < max(nums):
#             return False
        
#         nums.sort(reverse = True)
#         self.subset_sums = [0] * k
#         return self.dfs(nums, total / k, 0)
#     def dfs(self, nums, target, i):
#         if i == len(nums):
#             return True
#         for k in range(len(self.subset_sums)):
#             if self.subset_sums[k] + nums[i] > target:
#                 continue
#             self.subset_sums[k] += nums[i]
#             if self.dfs(nums, target, i + 1):
#                 return True
#             self.subset_sums[k] -= nums[i]
#             if not self.subset_sums[k]:
#                 return False
            
      
