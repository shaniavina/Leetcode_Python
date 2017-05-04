class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ways = [0] * n
        
        if obstacleGrid[0][0] == 0:
            ways[0] = 1
            
        for j in xrange(1, n):
            if obstacleGrid[0][j] == 1:
                ways[j] = 0
            else:
                ways[j] = ways[j - 1]
        
        for i in xrange(1, m):
            if obstacleGrid[i][0] == 1:
                ways[0] = 0
                
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    ways[j] = 0
                else:
                    ways[j] += ways[j - 1]
        
        return ways[n - 1]
