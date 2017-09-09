# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ###just traverse the tree and find if there is any node.val bigger than root.val
        self.res, self.min_1 = float('inf'), root.val
        self.traverse(root)
        return self.res if self.res != float('inf') else -1
    def traverse(self, node):
        if not node:
            return
        if self.min_1 < node.val < self.res:   ###global min_1
            self.res = node.val
        self.traverse(node.left)
        self.traverse(node.right)
        
