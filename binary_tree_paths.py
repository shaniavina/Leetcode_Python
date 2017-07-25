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
        #####preorder traverse
        result, path = [], ''
        self.binaryTreePathsRecu(root, path, result)
        return result
    
    def binaryTreePathsRecu(self, node, path, result):
        if not node:
            return
        
        path += str(node.val)
        
        if not node.left and not node.right:
            result.append(path)

        if node.left:
            self.binaryTreePathsRecu(node.left, path + '->', result)
           
        if node.right:
            self.binaryTreePathsRecu(node.right, path + '->', result)
           
