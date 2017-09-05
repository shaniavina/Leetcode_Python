# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        cur=TreeNode(-1)
        q=[root]
        while q:
            node = q.pop()
            cur.right = node
            cur.left = None
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            cur = node
