class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    temp = perm[i:] + [n] + perm[:i]
                    if temp not in new_perms:   ###solve the problem of duplicates
                        new_perms.append(temp)
            perms = new_perms
        return perms
