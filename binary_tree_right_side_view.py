# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        q, res = [root], []
        
        while q:
            next_q = []
            for tmp in q:
                if tmp.left:
                    next_q.append(tmp.left)
                if tmp.right:
                    next_q.append(tmp.right)
            
            res.append(tmp.val)   ##tmp is the last one in this level
            q = next_q
        return res
