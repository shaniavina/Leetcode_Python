class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(nums, pos, target):
            if pos == len(nums):
                return True
            for i in range(4):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(nums, pos + 1, target): return True
                    target[i] += nums[pos]
            return False
        
        if not nums:
            return False
        total_len = sum(nums)
        if total_len % 4:
            return False
        nums.sort(reverse = True)
        target = [total_len / 4] * 4
        return dfs(nums, 0, target)        
        
