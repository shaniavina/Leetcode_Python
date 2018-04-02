# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        
        min_cost = [costs[0], [0, 0, 0]]
        
        n = len(costs)
        for i in xrange(1, n):
            min_cost[i % 2][0] = costs[i][0] + \
                                 min(min_cost[(i - 1) % 2][1], min_cost[(i - 1) % 2][2])
            min_cost[i % 2][1] = costs[i][1] + \
                                 min(min_cost[(i - 1) % 2][0], min_cost[(i - 1) % 2][2])
            min_cost[i % 2][2] = costs[i][2] + \
                                 min(min_cost[(i - 1) % 2][0], min_cost[(i - 1) % 2][1])

        return min(min_cost[(n - 1) % 2])

###return the path
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        n = len(costs)
        min_cost = [[0 for i in range(3)] for j in range(n)]
        min_cost[0] = costs[0]
        
        for i in range(1, n):
            min_cost[i][0] = costs[i][0] + min(
                min_cost[i - 1][1], min_cost[i - 1][2])
            min_cost[i][1] = costs[i][1] +min(
                min_cost[i - 1][0], min_cost[i - 1][2])
            min_cost[i][2] = costs[i][2] + min(
                min_cost[i - 1][0], min_cost[i - 1][1])
                                
        res =  min(min_cost[n - 1])
        self.path = []
        for i in range(len(min_cost[n - 1])):
            if res == min_cost[n - 1][i]:
                self.path.append([i])
        self.minCostRecu(n - 1, min_cost)
        return self.path
    def minCostRecu(self, level, min_cost):
        if level == 0:
            return
        extended_path = []
        for p in self.path:
            if min_cost[level - 1][(p[-1] + 1) % 3] < min_cost[level - 1][(p[-1] + 2) % 3]:
                p.append((p[-1] + 1) % 3)
            elif min_cost[level - 1][(p[-1] + 1) % 3] > min_cost[level - 1][(p[-1] + 2) % 3]:
                p.append((p[-1] + 2) % 3)
            else:
                extended_path.append(p + [(p[-1] + 2) % 3])
                p.append((p[-1] + 1) % 3)
        self.path += extended_path
        self.minCostRecu(level - 1, min_cost)

slt = Solution()
costs = [[0,3,4], [2,5,2], [7,3,2], [4,5,2]]
print(slt.minCost(costs))
