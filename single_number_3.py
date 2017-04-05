class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [x[0] for x in sorted(collections.Counter(nums).items(), key = lambda i:i[1])[:2]]
