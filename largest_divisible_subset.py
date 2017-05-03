class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        dp = [1] * len(nums)
        pre = [-1] * len(nums)
        largestIndex = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        pre[i] = j
            if dp[largestIndex] < dp[i]:
                largestIndex = i
        res = []
        i = largestIndex
        while i != -1:
            res.append(nums[i])
            i = pre[i]
        return res[::-1]
