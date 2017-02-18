class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        count = {}
        
        for c in s:
            if c.lower() in count:                     ###.lower() not necessary
                count[c.lower()] += 1
            else:
                count[c.lower()] = 1
        
        for c in t:
            if c.lower() in count:
                count[c.lower()] -= 1
            else: 
                count[c.lower()] = -1
            if count[c.lower()] < 0:
                return False
                
        return True

                
###.lower() not necessary
