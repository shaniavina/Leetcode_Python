# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        cloned_node = UndirectedGraphNode(node.label)
        cloned = {node: cloned_node}
        queue = [node]
        
        while queue:
            cur = queue.pop()
            for neighbor in cur.neighbors:
                if neighbor not in cloned:
                    queue.append(neighbor)
                    cloned_neighbor = UndirectedGraphNode(neighbor.label)
                    cloned[neighbor] = cloned_neighbor
                cloned[cur].neighbors.append(cloned[neighbor])
                
        return cloned[node]   ###the way you want to save it
    
