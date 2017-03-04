# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def MinAbsoluteDistance(self, root):
        if not root:
            return sys.maxint, None, None
    
        left_child_min, left_left_most, left_right_most = self.MinAbsoluteDistance(root.left)
        right_child_min, right_left_most, right_right_most = self.MinAbsoluteDistance(root.right)
    
        left_root_min = abs(root.val - left_right_most.val) if  left_right_most else sys.maxint
        right_root_min = abs(root.val - right_left_most.val) if  right_left_most else sys.maxint
    
        return (min(left_child_min, right_child_min, left_root_min, right_root_min), 
                left_left_most if left_left_most else root, 
                right_right_most if right_right_most else root)

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.MinAbsoluteDistance(root)[0]
        
        
        
        ###########second solution
        def inorderTraversal(root, prev, result):
            if not root:
                return (result, prev)

            result, prev = inorderTraversal(root.left, prev, result)
            if prev: result = min(result, root.val - prev.val)
            return inorderTraversal(root.right, root, result)

        return inorderTraversal(root, None, float("inf"))[0]
