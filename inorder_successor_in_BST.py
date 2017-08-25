# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        # ###iteratively
        # if not root:
        #     return None
        # succ = None   ###set up null treenode
        # while root:
        #     if p.val < root.val:
        #         succ = root
        #         root = root.left
        #     else:
        #         root = root.right
        # return succ
        
        ###recursively
        if not root:
            return None
        if p.val < root.val:
            return self.inorderSuccessor(root.left, p) or root
        else:
            return self.inorderSuccessor(root.right, p)
        
        
