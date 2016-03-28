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
        '''
        def mirror(self, root):
        if not root:
            return root
        root.left, root.right = self.mirror(root.right), self.mirror(root.left)
        return root
        '''
        if not root:
            return True
        S1 = [root]
        S2 = [root]
        while S1 and S2:
            cur1 = S1.pop(0)
            cur2 = S2.pop(0)
            if (cur1 or cur2) and not (cur1 and cur2):
                return False
            if cur1 and cur2 and (cur1.val != cur2.val):
                return False
            if cur1:
                S1.append(cur1.left if cur1.left else None)
                S1.append(cur1.right if cur1.right else None)
            if cur2:
                S2.append(cur2.right if cur2.right else None)
                S2.append(cur2.left if cur2.left else None)
           
        return True
        
        
        ####solution2
         if root is None:
            return True
        
        return self.isSymmetricRecu(root.left, root.right)
    
    def isSymmetricRecu(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isSymmetricRecu(left.left, right.right) and self.isSymmetricRecu(left.right, right.left)
                
