# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res, cur, stk = [], root, []
        while cur or stk:
            if cur:
                stk.append(cur)
                cur = cur.left
            else:
                cur = stk.pop()
                res.append(cur.val)
                cur = cur.right
        return res[k - 1]
