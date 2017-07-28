# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        return self.pathSumRecu([], [], root, sum)
    
    def pathSumRecu(self, result, cur, root, sum):
        if not root:
            return result
        if not root.left and not root.right and root.val == sum:
            result.append(cur + [root.val])
            return result
        cur.append(root.val)
        self.pathSumRecu(result, cur, root.left, sum - root.val)
        self.pathSumRecu(result, cur, root.right, sum - root.val)
        cur.pop()
        return result

    
    ####almost the same
    # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        res = []
        self.pathSumRecu(root, sum, [], res)
        return res
        
    def pathSumRecu(self, node, sum, path, res):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right and node.val == sum:
            res.append(path + [])   ###append a list is a shallow copy; append a string or number is a deep copy
        
        if node.left:
            self.pathSumRecu(node.left, sum - node.val, path, res)
        if node.right:
            self.pathSumRecu(node.right, sum - node.val, path, res)
        path.pop()
            
