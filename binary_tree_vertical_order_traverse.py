# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = collections.deque([(root, 0)])   ####q = [(root, 0)]
        output = {}
        
        while len(q) > 0: 
            node, level = q.popleft()     ###q.pop(0)
            if level not in output:
                output[level] = [node.val]
            else:
                output[level].append(node.val)
            if node.left:
                q.append([node.left, level - 1])
            if node.right:
                q.append([node.right, level + 1])
        
        sortedkeys = sorted(output.keys())
        vert_order = []
        for i in sortedkeys:
            vert_order.append(output[i])
        return vert_order
            
            
        
