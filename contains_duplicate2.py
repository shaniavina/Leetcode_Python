class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_pos_map = {}
        for i in range(len(nums)):
            if (nums[i] in num_pos_map) and (i - num_pos_map[nums[i]] <= k):
                return True
            else:
                num_pos_map[nums[i]] = i
           
        return False
                
