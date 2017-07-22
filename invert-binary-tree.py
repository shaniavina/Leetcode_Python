# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
#         # Time:  O(n)
# # Space: O(h)
# # DFS, Recursive solution.
#         if not root:
#             return None
        
#         root.left = self.invertTree(root.right)
#         root.right = self.invertTree(root.left)
#         return root


    
    #####iterative impl. of pre-order traversal, stack
        if not root:
            return None
        nodes = [root]
        while nodes:
            node = nodes.pop()
            node.left, node.right = node.right, node.left
            if node.left:       #####have to make sure node.left exists
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return root
        
        
