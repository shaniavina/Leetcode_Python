# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, count):
        
        if root is None:
            return None
        if root.val in count:
            count[root.val] += 1
        else:
            count[root.val] = 1
        self.helper(root.left, count)
        self.helper(root.right, count)
        return 
    
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return []
        count = {}
        self.helper(root, count)
        max_freq = max(count.itervalues())
        res = [k for k, v in count.iteritems() if v == max_freq]
        return res
