class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum = grid[0]
        
        for i in range(1, len(grid[0])):
            sum[i] = sum[i - 1] + grid[0][i]
        for i in range(1, len(grid)):
            sum[0] += grid[i][0]
            for j in range(1, len(grid[0])):
                sum[j] = min(sum[j], sum[j - 1]) + grid[i][j]
        return sum[-1]
