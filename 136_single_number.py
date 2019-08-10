class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ####using set
        # lookup = set()
        # for num in nums:
        #     if num in lookup:
        #         lookup.remove(num)
        #     else:
        #         lookup.add(num)
        # return lookup.pop()
        
        
        res = 0
        for num in nums:
            res ^= num
        return res
                
