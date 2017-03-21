# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_level = 0
        self.val = None
        self.helper(root, 1)
        return self.val
    
    def helper(self, root, level):
        if not root:
            return
        if level > self.max_level:
            self.max_level = level
            self.val = root.val
        self.helper(root.left, level + 1)
        self.helper(root.right, level + 1)
