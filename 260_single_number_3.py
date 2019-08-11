class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor, a, b = 0, 0, 0
        for n in nums:
            xor ^= n
        mask = 1
        while (mask & xor == 0):
            mask <<= 1
        # partition into two groups
        for n in nums:
            if n & mask:
                a ^= n
            else:
                b ^= n
        return [a, b]
    
    
