class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = {'l': [-1, 0], 'r': [1, 0], 'u': [0, 1], 'd':[0, -1]}
        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                island = []
                if self.dfs(grid, i, j, island):
                    islands.add(''.join(island))
        return len(islands)
    
    def dfs(self, grid, i, j, island):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return False
        grid[i][j] = '#'
        for k, v in directions.iteritems():
            island.append(k)
            dfs(grid, i + v[0], j + v[1], island)
        return True
        
