# ####iteratively, use stacks
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stk, cur = [], [], root
        while stk or cur:
            if cur:
                stk.append((cur, False))   ####have to visit twice
                cur = cur.left
            else:
                (cur, b) = stk.pop()
                if b:
                    res.append(cur.val)
                    cur = None
                else:
                    stk.append((cur,True))
                    cur = cur.right

        return res        

    
    #####recursively

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.postorderTraversalRecu(root, res)
        return res
        
    def postorderTraversalRecu(self, cur, res):
        if cur:
            self.postorderTraversalRecu(cur.left, res)
            self.postorderTraversalRecu(cur.right, res)
            res.append(cur.val)
