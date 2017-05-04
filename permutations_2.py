class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solutions = [[]]
        
        for num in nums:
            next = []
            for sol in solutions:
                for i in range(len(sol) + 1):
                    candidate = sol[:i] + [num] + sol[i:]
                    if candidate not in next:
                        next.append(candidate)
            solutions = next
        return solutions
