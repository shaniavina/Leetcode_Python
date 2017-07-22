# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # ####recursion
        # if not root:
        #     return 0
        # if root.left and not root.left.left and not root.left.right:
        #     return root.left.val + self.sumOfLeftLeaves(root.right)
        # return self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)
        
        ####iteration, pre-order traversal, stack
        if not root:
            return 0
        res = 0
        nodes = [root]
        while nodes:
            node = nodes.pop()
            if node.left and not node.left.left and not node.left.right:
                res += node.left.val
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return res
