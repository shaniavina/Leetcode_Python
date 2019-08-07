# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time:  O(n)
# Space: O(h), h is height of binary tree
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBalancedRecu(root) >= 0
    def isBalancedRecu(self, root):
        if not root:
            return 0
        left = self.isBalancedRecu(root.left)    ####get depth
        right = self.isBalancedRecu(root.right)
        if left < 0 or right < 0 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1 
    
    
