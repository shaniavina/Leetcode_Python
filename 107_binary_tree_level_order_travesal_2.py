# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
####level order, BFS, queue
####reverse the result of 102
        if not root:
            return []
        q = [root]
        res = []
        while q:
            next_q = []
            tmp_res = []
            for node in q:
                tmp_res.append(node.val)
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            res.insert(0, tmp_res)
            q = next_q
        return res
        
