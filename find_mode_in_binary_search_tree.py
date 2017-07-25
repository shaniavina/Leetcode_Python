# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        #####using BST feature, inorder traversal
        #######doesn't work through
        pre, count, maxi, res = None, 0, 1, []
        classi = [pre, count, maxi, res]
        self.inorder(root, classi)
        return classi[3]
    
    def inorder(self, node, classi):
        if not node:
            return None
        self.inorder(node.left, classi)
        if classi[0]:
            if classi[0].val == node.val:
                classi[1] += 1
            else:
                classi[1] = 1
        if classi[1] >= classi[2]:
            if classi[1] > classi[2]:
                classi[3] = []
            classi[3].append(node.val)
            classi[2] = classi[1]
        classi[0] = node
        self.inorder(node.right, classi)
        
            
            
#         ####traverse, use hash table(extra space)
#         if not root:
#             return []
#         count = {}
#         self.findModeRecu(root, count)
#         max_freq = max(count.itervalues())
#         res = [k for k, v in count.iteritems() if v == max_freq]
#         return res
#     def findModeRecu(self, root, count):
#         if not root:
#             return None
#         if root.val in count:
#             count[root.val] += 1
#         else:
#             count[root.val] = 1
        
#         self.findModeRecu(root.left, count)
#         self.findModeRecu(root.right, count)
#         return
        
    
