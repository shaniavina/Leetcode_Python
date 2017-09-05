# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_int = 2 ** 31 - 1
        self.res = root.val   ###if there is only one root val
        self.maxPathSumRecu(root)
        return self.res
    def maxPathSumRecu(self, node):
        if not node:
            return 0
        left = max(0, self.maxPathSumRecu(node.left))
        right = max(0, self.maxPathSumRecu(node.right))
        self.res = max(self.res, node.val + left + right)
        return node.val + max(left, right)
    
    
   
