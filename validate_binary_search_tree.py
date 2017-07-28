# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pre = [None]
        return self.isValidBSTRecu(root, pre)     ###inorder traversal; pre is global variable; or you can return 'pre' in function
    def isValidBSTRecu(self, node, pre):
        if not node:
            return True
        if not self.isValidBSTRecu(node.left, pre):
            return False
        if pre[0] and node.val <= pre[0].val:
            return False
        pre[0] = node
        if not self.isValidBSTRecu(node.right, pre):
            return False
        return True
        
        #####amazing
    #     return self.isValidBSTRecu(root, float('-inf'), float('inf'))
    # def isValidBSTRecu(self, node, low, high):
    #     if not node:
    #         return True
    #     return low < node.val and node.val < high\
    #         and self.isValidBSTRecu(node.left, low, node.val) and self.isValidBSTRecu(node.right, node.val, high)
    
    
#     #####using stack 
#     class Solution:
#     def traverseBST(self, root):
#         if root == None:
#             return True
#         else:
#             n = root
#             stack = []
#             while n != None:
#                 stack.append(n)
#                 n = n.left
            
#             pre = None
#             while len(stack):
#                 n = stack.pop()
#                 if pre != None:
#                     if pre >= n.val:
#                         return False
#                 pre = n.val
                
#                 if n.right != None:
#                     nr = n.right
#                     while nr != None:
#                         stack.append(nr)
#                         nr = nr.left
#             return True
#     # @param root, a tree node
#     # @return a boolean
#     def isValidBST(self, root):
#         return self.traverseBST(root)
    
    
