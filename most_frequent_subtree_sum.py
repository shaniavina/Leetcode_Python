# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        def getSum(node):
            if not node:
                return 0
            sumi = node.val + getSum(node.left) + getSum(node.right)
            mapi[sumi] += 1
            return sumi
        
        mapi = collections.defaultdict(int)
        getSum(root)
        max_count = max(mapi.itervalues())
        return [k for k, v in mapi.iteritems() if v == max_count]
        
    
