# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        previous = (None, -1)
        result = []
        queue = [(root, 0)]
        currentLevel = []
        
        while len(queue) > 0:
            current = queue.pop(0)
            if previous[1] < current[1]:
                result.append(currentLevel)
                currentLevel = [current[0].val]
            else:
                currentLevel.append(current[0].val)
                
            if current[0].left != None:
                queue.append((current[0].left, current[1] + 1))
            if current[0].right != None:
                queue.append((current[0].right, current[1] + 1)) 
            previous = current
        
        result.append(currentLevel)
        result = result[1:]
        result.reverse()
        return result
