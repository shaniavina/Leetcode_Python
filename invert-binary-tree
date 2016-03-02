# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        else:
            invertedLeft = self.invertTree(root.left)
            invertedRight = self.invertTree(root.right)
            
            root.left = invertedRight
            root.right = invertedLeft
            
            return root
