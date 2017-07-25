# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.pathSumRecu(root, 0, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    def pathSumRecu(self, node, pre, sum):
        if not node:
            return 0
        cur = pre + node.val
        return int(cur == sum) + self.pathSumRecu(node.left, cur, sum) + self.pathSumRecu(node.right, cur, sum)
    
    
