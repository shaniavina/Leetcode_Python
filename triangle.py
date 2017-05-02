class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        res = triangle[-1]
        for i in reversed(range(len(triangle) - 1)):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]
