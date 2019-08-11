class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0
        for n in nums:
            ones = (ones ^ n) & ~ twos
            twos = (twos ^ n) & ~ ones
        return ones
