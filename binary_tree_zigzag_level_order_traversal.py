# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        self.zigzagLevelOrderRecu(root, 0)
        return self.res
    def zigzagLevelOrderRecu(self, node, level):
        if not node:
            return 
        if len(self.res) == level:
            self.res.append([node.val])
        elif level % 2:
            self.res[level].insert(0, node.val)
        else:
            self.res[level].append(node.val)
        self.zigzagLevelOrderRecu(node.left, level + 1)
        self.zigzagLevelOrderRecu(node.right, level + 1)
        
        
        
#         ####QUEUE
#         if not root:
#             return []
#         q = collections.deque([root])
#         res = []
#         level = 1   ####level parameter to control the output order
#         while q:
#             next_q = collections.deque([])
#             tmp = []
#             for node in q:
#                 tmp.append(node.val)
#                 if node.left:
#                     next_q.append(node.left)
#                 if node.right:
#                     next_q.append(node.right)
#             if level % 2:
#                 res.append(tmp)
#             else:
#                 res.append(tmp[::-1])
#             level += 1
#             q = next_q
#         return res
    
    
