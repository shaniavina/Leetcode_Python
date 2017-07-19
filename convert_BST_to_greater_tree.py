# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def __init__(self):
    #     self.sum = 0      #######sum == 0 for the beginning
    # def convertBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: TreeNode
    #     """
    #     ####in order traversal(recursion, iteration[stack]), this one doesn't need helper funciton, better!!
    #     if not root:
    #         return None
    #     self.convertBST(root.right)
    #     root.val += self.sum
    #     self.sum = root.val
    #     self.convertBST(root.left)
    #     return root
    
    
    #####recursion, helper, reverse inorder traversal
    def convertBST(self, root):

        self.convertBSTHelper(root, 0)
        return root
    def convertBSTHelper(self, root, sum):
        if not root:
            return sum
        if root.right:
            sum = self.convertBSTHelper(root.right, sum)
        root.val += sum
        sum = root.val
        if root.left:
            sum = self.convertBSTHelper(root.left, sum)
        return sum
