class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        lookup = {}
        for num in nums:
            if num in lookup:
                lookup[num] += 1
            else:
                lookup[num] = 1
        
        res = 0
        for key in lookup:
            if key + 1 in lookup:
                res = max(res, lookup[key] + lookup[key + 1])
        return res
        
        
        
        #####better
        res = 0
        lookup = collections.defaultdict(int)     #####lookup setup
        for num in nums:
            lookup[num] += 1
            for diff in [-1, 1]:
                if num + diff in lookup:    
                    res = max(res, lookup[num] + lookup[num + diff])
        return res
