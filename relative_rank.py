class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        rank_map = {}
        nums_sorted = sorted(nums)
        if len(nums) >= 1:
            rank_map[nums_sorted[-1]] = "Gold Medal"
            if len(nums) >= 2:
                rank_map[nums_sorted[-2]] = "Silver Medal"
                if len(nums) >= 3:
                    rank_map[nums_sorted[-3]] = "Bronze Medal"
                    
        for i in range(4, len(nums) + 1):
            rank_map[nums_sorted[len(nums) - i]] =  str(i)
    
        
        return [rank_map[nums[i]] for i in range(len(nums))]
        
        
