"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # if root and root.left and root.right:
        #     root.left.next = root.right
        #     if root.next:
        #         root.right.next = root.next.left
        #     self.connect(root.left)
        #     self.connect(root.right)
        # return root
        
        # BFS
        if not root:
            return
        queue = [root]
        while queue:
            cur = queue.pop(0)
            if cur.left and cur.right:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                queue.append(cur.left)
                queue.append(cur.right)
        return root
