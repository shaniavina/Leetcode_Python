class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):  ####have to compare the length first
            return False
        
        lookup = {}
        for w in s:
            if w in lookup:
                lookup[w] += 1
            else:
                lookup[w] = 1
        
        for c in t:
            if c not in lookup or lookup[c] == 0:
                return False
            else:
                lookup[c] -= 1
        return True
            
