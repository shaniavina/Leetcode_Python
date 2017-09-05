# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ###Recursion
        if not root:    ####have to discuss this 
            return 0
        
        self.res = 1
        self.longestConsecutiveRecu(root, 1)
        return self.res
    
    def longestConsecutiveRecu(self, node, l):
        if not node:
            return
        
        for child in (node.left, node.right):
            if child:
                if child.val == node.val + 1:
                    self.res = max(self.res, l + 1)
                    self.longestConsecutiveRecu(child, l + 1)
                else:
                    self.longestConsecutiveRecu(child, 1)


        
        
        # ###iteratively
        # if not root:
        #     return 0
        # res, stk = 0, [[root, 1]]
        # while stk:
        #     node, length = stk.pop()
        #     res = max(res, length)
        #     if node.left:
        #         l = length + 1 if node.val + 1 == node.left.val else 1
        #         stk.append([node.left, l])
        #     if node.right:
        #         l = length + 1 if node.val + 1 == node.right.val else 1
        #         stk.append([node.right, l])
        # return res
