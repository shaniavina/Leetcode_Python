class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        last, i, same = 0, 1, False
        while i < len(nums):
            if nums[i] != nums[last] or not same:
                same = nums[i] == nums[last]
                last += 1
                nums[last] = nums[i]
            i += 1  ### why for not working while while works?
        return last + 1
        

      
