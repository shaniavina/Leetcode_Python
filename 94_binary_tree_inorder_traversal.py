# ####iteratively, use stacks
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res,stack,cur = [],[],root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res
    
    ######recursively

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.inorderTraversalRecu(root, res)
        return res
        
    def inorderTraversalRecu(self, cur, res):
        if cur:
            self.inorderTraversalRecu(cur.left, res)
            res.append(cur.val)
            self.inorderTraversalRecu(cur.right, res)
            
