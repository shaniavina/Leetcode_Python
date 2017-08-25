class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        ###space: O(1), reuse preorder: using index to move 
       
        lower, i = float('-inf'), -1
        for x in preorder:
            if x < lower:
                return False
            while i >= 0 and preorder[i] < x:
                lower = preorder[i]
                i -= 1
            i += 1
            preorder[i] = x
        return True
        
        
        
        
#         ##space: O(n)
#         stack = []
#         lower = -1 << 31
#         for x in preorder:
#             if x < lower:
#                 return False
#             while stack and x > stack[-1]:
#                 lower = stack.pop()
#             stack.append(x)
#         return True
