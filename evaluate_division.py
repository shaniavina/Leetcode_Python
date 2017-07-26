class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        lookup = collections.defaultdict(dict)
        for i, e in enumerate(equations):
            lookup[e[0]][e[1]] = values[i]
            if values[i]:
                lookup[e[1]][e[0]] = 1.0 / values[i]
        res = []
        for q in queries:
            visited = set()
            tmp = self.check(q[0], q[1], lookup, visited)
            res.append(tmp[1] if tmp[0] else -1.0)
        return res
    
    def check(self, up, down, lookup, visited):
        
        if up in lookup and down in lookup[up]:
            return [True, lookup[up][down]]
        for k, v in lookup[up].iteritems():
            if k not in visited:
                visited.add(k)
                tmp = self.check(k, down, lookup, visited)
                if tmp[0]:
                    return [True, v * tmp[1]]
        return [False, 0]
    
    #####second, using graph, BFS, queue, to be completed
