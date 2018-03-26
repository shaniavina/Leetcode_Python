# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        q = [root]
        while q:
            node = q.pop(0)
            if node:
                q.append(node.left)
                q.append(node.right)
                res.append(node.val)
            else:
                res.append(None)
        while res and res[-1] == None:
            res.pop()
            
        return res
    
    def deserialize(self, data):
        if not data:
            return None
        root = TreeNode(data[0])
        q = [root]
        idx = 1
        
        while q:
            next_q = []
            for node in q:
                if idx < len(data):
                    if data[idx] != None:
                        node.left = TreeNode(data[idx])
                        next_q.append(node.left)
                    idx += 1
                    if idx < len(data):
                        if data[idx] != None:
                            node.right = TreeNode(data[idx])
                            next_q.append(node.right)
                        idx += 1
            q = next_q
        return root
                        
                    
        
