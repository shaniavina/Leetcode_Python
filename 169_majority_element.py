

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        for key in count:
            if count[key] >= (len(nums) + 1) / 2:
                return key

        #### NOTICE that the majority element always exist in the array,so that the middle always is the answer
        return sorted(num)[len(num)/2]
