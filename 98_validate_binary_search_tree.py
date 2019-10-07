# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ####amazing
        return self.isValidBSTRecu(root, float('-inf'), float('inf'))
    def isValidBSTRecu(self, node, low, high):
        if not node:
            return True
        return low < node.val and node.val < high\
            and self.isValidBSTRecu(node.left, low, node.val) and self.isValidBSTRecu(node.right, node.val, high)
    
