# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.postOrderTraverse(root)
        return self.res
    
    def postOrderTraverse(self, node):       #####post order traverse
        if not node:
            return 0
        left = self.postOrderTraverse(node.left)
        right = self.postOrderTraverse(node.right)
        self.res += abs(left - right)
        return left + right + node.val
    
