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
        ####recursion, (root, level, res)
        res = []
        self.levelOrderRecu(root, 0, res)
        return res
    def levelOrderRecu(self, root, level, res):
        if not root:
            return
        if len(res) == level:
            res.append([root.val])
        else:
            res[level].append(root.val)
        self.levelOrderRecu(root.left, level + 1, res)
        self.levelOrderRecu(root.right, level + 1, res)
    
#         ####level order, BFS, queue
#         if not root:
#             return []
#         q = [root]
#         res = []
        
#         while q:
#             next_q = collections.deque([])
#             tmp_res = []
#             for node in q:
#                 tmp_res.append(node.val)
#                 if node.left:
#                     next_q.append(node.left)
#                 if node.right:
#                     next_q.append(node.right)
#             res.append(tmp_res)
#             q = next_q
#         return res
        
