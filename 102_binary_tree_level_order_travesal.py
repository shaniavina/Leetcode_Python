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
    #     # recursion
    #     res = []
    #     self.levelOrderRecu(root, 0, res)
    #     return res
    # def levelOrderRecu(self, node, level, res):
    #     if not node:
    #         return
    #     if len(res) == level:
    #         res.append([node.val])
    #     else:
    #         res[level].append(node.val)
    #     self.levelOrderRecu(node.left, level + 1, res)
    #     self.levelOrderRecu(node.right, level + 1, res)
    
        
        
        ### stack, BFS
        if not root:
            return []
        q = [root]
        res = []
        while q:
            next_q = []
            tmp = []
            for node in q:
                tmp.append(node.val)
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            res.append(tmp)
            q = next_q
        return res
