class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ####topological sort + graph theory, BFS, peeled onions
        if n == 1:
            return [0]
        
        neighbors = collections.defaultdict(set)
        for u, v in edges:
            neighbors[u].add(v)
            neighbors[v].add(u)
        
        pre_level, unvisited = [], set()
        for i in range(n):
            if len(neighbors[i]) == 1:   ###leaf
                pre_level.append(i)
            unvisited.add(i)
            
        while len(unvisited) > 2:
            cur_level = []
            for u in pre_level:
                unvisited.remove(u)
                for v in neighbors[u]:
                    neighbors[v].remove(u)
                    if len(neighbors[v]) == 1:   #####what if there is no such points, then choose the least linked ones
                        cur_level.append(v)
            pre_level = cur_level
        return list(unvisited)
