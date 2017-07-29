class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        ##cycle detection(DFS)
        adj = [[] for i in range(numCourses)] #####bloody lesson
        for i, j in prerequisites:
            adj[i].append(j)
        visited = [0] * numCourses
        
        for i in range(numCourses):
            if visited[i] > 0:
                continue
            if not self.canFinishRecu(numCourses, adj, i, visited):
                return False
        return True
    def canFinishRecu(self, numCourses, adj, v, visited):
        visited[v] = 1
        for j in adj[v]:
            if visited[j] == 1:
                return False
            if visited[j] == 0 and not self.canFinishRecu(numCourses, adj, j, visited):
                return False
        visited[v] = 2
        return True
           

        
        
#         #topological sort (BFS)
#         ###build up directed graphs, Queue
#         in_degree, out_degree = collections.defaultdict(set), collections.defaultdict(set)
#         zero_in_queue = collections.deque()
#         for i, j in prerequisites:
#             in_degree[i].add(j)
#             out_degree[j].add(i)
#         for i in range(numCourses):
#             if i not in in_degree:
#                 zero_in_queue.append(i)
                
#         while zero_in_queue:
#             cur = zero_in_queue.popleft()
#             if cur in out_degree:   ####have to make sure it is not a independent point
#                 for u in out_degree[cur]:
#                     in_degree[u].remove(cur)
#                     if not in_degree[u]:
#                         zero_in_queue.append(u)
#                 del out_degree[cur]    ####delete all the outgoing pointer
#         if out_degree:   ####there should be no outing going pointer any more if it is not a cycle
#             return False
#         return True
