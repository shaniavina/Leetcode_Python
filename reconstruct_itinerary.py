class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        ###post-order, recursion
        graph = collections.defaultdict(list)
        for i, j in tickets:
            graph[i].append(j)
        for k in graph.keys():
            graph[k].sort()
        
        res = []
        self.findItineraryRecu('JFK', graph, res)
        res.reverse()
        return res
    
    def findItineraryRecu(self, origin, graph, res):
        cur = graph[origin]
        while cur:
            next = cur.pop(0)
            self.findItineraryRecu(next, graph, res)
        res.append(origin)
        
        
        ###post-order, iteration
#         graph = collections.defaultdict(list)
#         for i, j in tickets:
#             graph[i].append(j)
#         for k in graph.keys():
#             graph[k].sort()
#         stk, res = ['JFK'], []
        
#         while stk:
#             cur = stk[-1]     #####bloody lesson
#             next = graph[cur]
#             if next:
#                 stk.append(next.pop(0))
#             else:
#                 stk.pop()
#                 res.append(cur)
#         res.reverse()
#         return res
        

        
        
        ##directed graph traverse, recursion
        #graph
#         graph = collections.defaultdict(list)
#         for i, j in tickets:
#             graph[i].append([j, True])
#         for k in graph.keys():
#             graph[k].sort()
            
#         origin  ='JFK'
#         res = [origin]
#         self.findItineraryRecu(origin, len(tickets), graph, res)
#         return res
    
#     def findItineraryRecu(self, origin, ticket_cnt, graph, res):
#         if ticket_cnt == 0:
#             return True
#         for i, (dest, valid)  in enumerate(graph[origin]):
#             if valid:
#                 graph[origin][i][1] = False
#                 res.append(dest)
#                 if self.findItineraryRecu(dest, ticket_cnt - 1, graph, res):
#                     return res
#                 res.pop()
#                 graph[origin][i][1] = True
#         return False
