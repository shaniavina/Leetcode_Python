# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        self.res = []
        self.findLeavesRecu(root)
        return self.res
    def findLeavesRecu(self, node):
        if not node:
            return -1
        level = 1 + max(findLeavesRecu(node.left) +  findLeavesRecu(node.right))
        if len(self.res) < level + 1:
            self.res.append([])
        self.res[level].append(node.val)
        return level
    
    
####second
class Solution(object):
    def findLeaves(self, root):
        res = []
        self.findLeavesRecu(root, res)
        return res
    def findLeavesRecu(self, node, res):
        if not node:
            return -1
        level = 1 + max(self.findLeavesRecu(node.left, res) +  
                        self.findLeavesRecu(node.right), res)
        if len(res) < level + 1:
            res.append([])
        res[level].append(node.val)
        return level
