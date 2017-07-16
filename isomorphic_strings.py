class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
#         if len(s) != len(t):
#             return False
#         return self.halfIsom(s, t) and self.halfIsom(t, s)
    
    
#     def halfIsom(self, s, t):
#         lookup = {}
#         for i in range(len(s)):
#             if s[i] in lookup:
#                 if lookup[s[i]] != t[i]:
#                     return False
#             else:
#                 lookup[s[i]] = t[i]
#         return True        ######have to do the halfIsom if you only set up one hash table

        #####second
        if len(s) != len(t):
            return False
        map1 = {}
        map2 = {}
        for i in range(len(s)):
            if s[i] in map1:
                if map1[s[i]] != t[i]:
                    return False
            else:
                map1[s[i]] = t[i]
                
            if t[i] in map2:
                if map2[t[i]] != s[i]:
                    return False
            else:
                map2[t[i]] = s[i]
        return True
