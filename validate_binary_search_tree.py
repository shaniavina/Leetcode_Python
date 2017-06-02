# in order traversal
####doesn't work if you have duplicate values

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pre = float('-inf')
        return self.isValidBSTRecu(root, pre)
    def isValidBSTRecu(self, root, pre):
        if not root:
            return True
        if not self.isValidBSTRecu(root.left, pre):
            return False
        if not pre and root.val <= pre:
            return False
        pre = root.val
        if not self.isValidBSTRecu(root.right, pre):
            return False
        return True
  
  
  
  ######min and max
  
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.isValidBSTRecu(root, float("-inf"), float("inf"))
        
    def isValidBSTRecu(self, root, low, high):
        if not root:
            return True
        return low < root.val and root.val < high \
            and self.isValidBSTRecu(root.left, low, root.val) \
            and self.isValidBSTRecu(root.right, root.val, high)
            
