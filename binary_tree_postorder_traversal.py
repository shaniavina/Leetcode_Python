# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stk, cur = [], [], root
        while stk or cur:
            if cur:
                stk.append((cur, False))
                cur = cur.left
            else:
                (cur, b) = stk.pop()
                if b:
                    res.append(cur.val)
                    cur = None
                else:
                    stk.append((cur,True))
                    cur = cur.right

        return res        
