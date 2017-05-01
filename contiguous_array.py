class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, cur_sum = 0, 0
        lookup = {0:-1}
        for i, num in enumerate(nums):
            if num == 1:
                cur_sum += 1
            else:
                cur_sum -= 1
            if cur_sum in lookup:
                result = max(result, i - lookup[cur_sum])
            else:
                lookup[cur_sum] = i   ####write down current sum and the corresponding index
        return result
            
