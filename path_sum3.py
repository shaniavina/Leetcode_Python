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
        return self.helper(root, 0, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        
    def helper(self, root, pre, sum):
        if not root:
            return 0
        cur = pre + root.val
        return int(cur == sum) + self.helper(root.left, cur, sum) + self.helper(root.right, cur, sum)
    
