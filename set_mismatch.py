class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        numSet = set()
        for num in nums:
            if num not in numSet:
                numSet.add(num)
            else:
                res.append(num)
        missing = sum(range(1, len(nums) + 1)) - sum(nums) + res[0]
        res.append(missing)
        return res
