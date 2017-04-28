class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        used = [False] * len(nums)
        self.permuteHelper(result, used, [], nums)
        return result
    def permuteHelper(self, result, used, cur, nums):
        if len(cur) == len(nums):
            result.append(cur + [])
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                cur.append(nums[i])
                self.permuteHelper(result, used, cur, nums)
                cur.pop()
                used[i] = False
