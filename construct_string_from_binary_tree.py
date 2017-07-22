# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
#####recursion        
        if not t:
            return ''
        s = str(t.val)
        if t.left or t.right:
            s += '(' + self.tree2str(t.left) + ')'
        if t.right:
            s += '(' + self.tree2str(t.right) + ')'
        return s


