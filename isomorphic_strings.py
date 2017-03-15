class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
            
        if len(s) == len(t) and len(s) == 0:
            return True
        
        n = len(s)
        map1 = {}
        map2 = {}
        for i in range(n):
            c1 = s[i]
            c2 = t[i]
            if c1 in map1:
                if c2 != map1[c1]:
                    return False
            else:
                map1[c1] = c2
                
            if c2 in map2:
                if c1 != map2[c2]:
                    return False
            else:
                map2[c2] = c1
        return True
    
