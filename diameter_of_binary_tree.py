# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.best = 0
        self.map = {}
        self.depth(root)
        return self.best
    
    def depth(self, root):
        if not root:
            return 0
        if root in self.map:      ######optimization, using hash table
            return self.map[root]
        
        left = self.depth(root.left)
        right = self.depth(root.right)
        self.best = max(self.best, left + right)
        self.map[root] = 1 + max(left, right)
        return self.map[root]
