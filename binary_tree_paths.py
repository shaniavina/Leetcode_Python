# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result, path = [], []
        self.binaryTreePathsRecu(root, path, result)
        return result
    
    def binaryTreePathsRecu(self, node, path, result):
        if node is None:
            return

        if node.left is None and node.right is None:
            ans = ""
            for n in path:
                ans += str(n.val) + "->"
            result.append(ans + str(node.val))
#######result = ...+ .... not okay??
        if node.left:
            path.append(node)
            self.binaryTreePathsRecu(node.left, path, result)
            path.pop()

        if node.right:
            path.append(node)
            self.binaryTreePathsRecu(node.right, path, result)
            path.pop()
