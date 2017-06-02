# ####iteratively, use stacks

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack, cur = [],[],root
        while stack or cur:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                cur = cur.right
        return res

    
    #####recursively 

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.preorderTraversalRecu(root, res)
        return res
        
    def preorderTraversalRecu(self, cur, res):
        if cur:
            res.append(cur.val)
            self.preorderTraversalRecu(cur.left, res)
            self.preorderTraversalRecu(cur.right, res)
