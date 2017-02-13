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
        
        
###solution two

i_l = [(v,i) for i,v in enumerate(nums)]
        i_l.sort(key = lambda x:x[0])
        
        first_three = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        
        ret = [''] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i >= len(nums) - 3:
                ret[i_l[i][1]] = first_three[len(nums) - i - 1]
            else:
                ret[i_l[i][1]] = str(len(nums) - i)
        return ret
        
