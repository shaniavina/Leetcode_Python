class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) > len(set(nums))

###second solution

        count = {}
        
        for num in nums:
            if num in count:
                return True;
            else:
                count[num] = 1
        return False
            
