# iteratively: BFS

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []   ####base case
        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)
        return result
    
    ####recursively
    # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
    
        res = []
        self.levelOrderRecu(root, res, 0)
        return res
        
    def levelOrderRecu(self, root, res, level):
        if not root:
            return None
        
        if len(res) == level:  ####level not contained in list
            res.append([root.val])
        else:
            res[level].append(root.val)
        
        self.levelOrderRecu(root.left, res, level + 1)
        self.levelOrderRecu(root.right, res, level + 1)
        
        

    
