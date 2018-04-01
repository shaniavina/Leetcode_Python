
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # trivial case one subset
        if k==1: return True
        # trivial case, k must be k<=n
        n= len(nums)
        if k>n: return False
        # k*target = sum(nums)
        total = sum(nums)
        if total%k: return False
        
        target = total/k
        seen = [0]*n
        # speeds things up, as larger numbers are tried first if its not possible
        # to get k subsets we will know sooner
        nums.sort(reverse=True)
        
        def dfs(k,index,current_sum):
            # trivial, one group
            if k==1: return True
            # found one group, need more k-1 groups
            if current_sum == target:
                return dfs(k-1,0,0)
            # group can start with any number
            for i in range(index,n):
                # if we have not tried it before, and adding it 
                # to current sum does not exceed target then
                if not seen[i] and current_sum+nums[i]<=target:
                    # we have seen it 
                    seen[i]=1
                    # recursively build group from i+1
                    if dfs(k,i+1,current_sum+nums[i]):
                        return True
                    seen[i]=0
            return False
        
        return dfs(k,0,0)
        
        


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
            
      
