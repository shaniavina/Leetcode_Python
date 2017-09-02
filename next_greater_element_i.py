class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        lookup = {}
        tmp, res = [], []
        
        for x in nums:
            while len(tmp) and tmp[-1] < x:
                lookup[tmp.pop()] = x
            tmp.append(x)
        
        for x in findNums:
            res += [lookup.get(x, -1)]    ####append(x)  or res += [x]
        return res
