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
        self.maxi = float('-inf')
        self.maxPathSumRecu(root, self.maxi)
        return self.maxi
    def maxPathSumRecu(self, root, maxi):
        if not root:
            return 0
        left = self.maxPathSumRecu(root.left, self.maxi)
        right = self.maxPathSumRecu(root.right, self.maxi)
        
        left = 0 if (left is None or left <= 0) else left
        right = 0 if (right is None or right <= 0) else right
        
        self.maxi = max(self.maxi, left + right + root.val)
        return max(left, right) + root.val
