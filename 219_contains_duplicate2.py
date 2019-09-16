class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
####mine
lookup = {}
        for i, num in enumerate(nums):
            if num in lookup and (i - lookup[num]) <= k:
                return True
            else:
                lookup[num] = i
        return False
