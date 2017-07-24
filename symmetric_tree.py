# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #######iteration with stack
        if not root:
            return True
        stk = [(root.left, root.right)]
        while stk:
            node = stk.pop()
            node1 = node[0]
            node2 = node[1]
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            stk.append((node1.left, node2.right))
            stk.append((node1.right, node2.left))
            
        return True
        
#         #####recursion
#         if not root:
#             return True
#         return self.isSymmetricRecu(root.left, root.right)
    
#     def isSymmetricRecu(self, left, right):
#         if not left and not right:
#             return True
#         if not left or not right or left.val != right.val:
#             return False
#         return self.isSymmetricRecu(left.left, right.right) and self.isSymmetricRecu(left.right, right.left)


        
        
