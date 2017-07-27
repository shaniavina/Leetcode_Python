# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # Time:  O(n)
# Space: O(h)
####level order traversal, queue, next_q
        if not root:
            return None
        q = collections.deque([root])
        res = []
        
        while q:
            total, count = 0, 0
            next_q = collections.deque([])
            while q:
                n = q.popleft()
                total += n.val
                count += 1
                if n.left:
                    next_q.append(n.left)
                if n.right:
                    next_q.append(n.right)
            q, next_q = next_q, q
            res.append(float(total) / count)
        return res
