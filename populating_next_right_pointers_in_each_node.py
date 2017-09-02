# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return 
        q, next_q = [root], []
        
        while q:
            tmp = q.pop(0)
            if tmp.left:
                next_q.append(tmp.left)
            if tmp.right:
                next_q.append(tmp.right)
            if q:
                tmp.next = q[0]
            if not q and next_q:
                q, next_q = next_q, q    ###next_q = q becuz next_q has to be None
