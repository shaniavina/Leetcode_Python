class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                cnt += 1
                if cnt > 1:
                    return False
                if i < 2 or nums[i - 2] <= nums[i]:
                    # from 3 1 2 to 3 2 2
                    nums[i - 1] = nums[i]
                else:
                    # from 2 1 3 to 2 1 1
                    nums[i] = nums[i - 1]
        return True
