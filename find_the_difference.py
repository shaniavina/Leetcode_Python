class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_map = {}
        for l in s:
            if l in s_map:
                s_map[l] += 1
            else:
                s_map[l] = 1

        t_map = {}
        for l in t:
            if l in t_map:
                t_map[l] += 1
            else:
                t_map[l] = 1
                
        for l in t_map:
            if t_map[l] != s_map.get(l, 0):    ####dict.get(key, defaultValue), return defaultValue if dict[key] is missing
                return l
                
        
          ###second solution 
    def findTheDifference2(self, s, t):
         s_sorted = sorted(s)
        t_sorted = sorted(t)
        
        for i in range(len(s)):
            if s_sorted[i] != t_sorted[i]:
                return t_sorted[i]
        return t_sorted[-1]
