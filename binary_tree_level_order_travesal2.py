# iteratively

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
         if not root:
            return []
        current_level = -1
        queue = [(root, 0)]    #####tuple (node, level)
        res = []
        while queue:
            node, level = queue.pop(0)
            if current_level < level:
                res.insert(0, [node.val])   #####instead of .reverse(), you can use insert on the top of queue
                current_level = level
            else:
                res[0].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return res
