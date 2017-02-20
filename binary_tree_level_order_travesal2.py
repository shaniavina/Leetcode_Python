# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
         if not root:
            return []
        current_level = -1
        queue = [(root, 0)]    #####tuple (node, level)
        res = []
        while queue:
            node, level = queue.pop(0)
            if current_level < level:
                res.insert(0, [node.val])   #####instead of .reverse()
                current_level = level
            else:
                res[0].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return res
