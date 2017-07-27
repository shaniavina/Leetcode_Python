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
        if not root:
            return []
        q = [root]
        res = []
        level = 1   ####level parameter to control the output order
        while q:
            next_q = collections.deque([])
            tmp_res = []
            
            for node in q:
                tmp_res.append(node.val)
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            if level % 2:
                res.append(tmp_res)
            else:
                res.append(tmp_res[::-1])
                
            level += 1
            q = next_q
        
        return res
