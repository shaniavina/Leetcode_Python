# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
    #     ####recursion, (root, level)
    #     self.res = []
    #     self.levelOrderRecu(root, 0)
    #     return self.res
    # def levelOrderRecu(self, node, level):
    #     if not node:
    #         return
    #     if len(self.res) == level:
    #         self.res.append([node.val])
    #     else:
    #         self.res[level].append(node.val)
    #     self.levelOrderRecu(node.left, level + 1)
    #     self.levelOrderRecu(node.right, level + 1)
      
    
# #         ####level order, BFS, queue
#         if not root:
#             return []
#         q = collections.deque([root])
#         res = []
#         while q:
#             next_q = collections.deque([])
#             tmp = []
#             for node in q:
#                 tmp.append(node.val)
#                 if node.left:
#                     next_q.append(node.left)
#                 if node.right:
#                     next_q.append(node.right)
#             res.append(tmp)
#             q = next_q
#         return res
