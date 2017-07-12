class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         sorted_nums = sorted(nums)
#         if sorted_nums == nums:
#             return 0
#         left, right = 0, len(nums) - 1
#         for i in range(len(nums)):
#             if sorted_nums[i] != nums[i]:
#                 left = i
#                 break
#         for j in reversed(range(left + 1, len(nums))):
#             if sorted_nums[j] != nums[j]:
#                 right = j
#                 break
#         res = right - left + 1
#         return res
        
        n = len(nums)
        left, right = -1, -2
        max_from_left, min_from_right = nums[0], nums[-1]
        for i in range(1, n):
            max_from_left = max(max_from_left, nums[i])
            min_from_right = min(min_from_right, nums[n - 1 - i])
            if nums[i] < max_from_left:
                right = i
            if nums[n - 1 - i] > min_from_right:
                left = n - 1 - i
        return right - left + 1
