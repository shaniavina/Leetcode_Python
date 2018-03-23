# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.largestValuesRecu(root, 0)
        return self.res
    def largestValuesRecu(self, node, level):
        if not node:
            return
        if len(self.res) == level:
            self.res.append(node.val)
        else:
            self.res[level] = max(self.res[level], node.val)  ###for choose only one maximum one value
        self.largestValuesRecu(node.left, level + 1)
        self.largestValuesRecu(node.right, level + 1)
        
        # if not root:
        #     return []
        # q = collections.deque([root])
        # res = []
        # while q:
        #     next_q = collections.deque([])
        #     temp = []
        #     for node in q:
        #         temp.append(node.val)
        #         if node.left:
        #             next_q.append(node.left)
        #         if node.right:
        #             next_q.append(node.right)
        #     res.append(max(temp))
        #     q = next_q
        # return res
