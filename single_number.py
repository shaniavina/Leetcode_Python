class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # lookup = {}
        # for num in nums:
        #     if num in lookup:
        #         lookup[num] += 1
        #     else:
        #         lookup[num] = 0
        # for key in lookup:
        #     if lookup[key] == 0:
        #         return key
        
        
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
                
