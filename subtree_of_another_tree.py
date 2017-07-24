# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t:
            return True
        if not s:
            return False
        if self.isSameTree(s,t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if s and t:
            return s.val == t.val and self.isSameTree(s.right, t.right) and self.isSameTree(s.left, t.left)
        return False



######serialize and deserialize binary tree
    
