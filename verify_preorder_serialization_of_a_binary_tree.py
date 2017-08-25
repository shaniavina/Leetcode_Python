class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return False
        
        depth, cnt = 0, preorder.count(',') + 1
        for c in preorder.split(','):
            cnt -= 1
            if c == '#':
                depth -= 1
                if depth < 0:
                    break
            else:
                depth += 1
        return cnt == 0 and depth < 0

    
