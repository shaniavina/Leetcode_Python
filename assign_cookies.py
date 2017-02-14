class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        c = 0
        k = 0
        count = 0
        while c <= k and k < len(s) and c < len(g):
            if s[k] >= g[c]:
                count += 1
                c += 1
                k += 1
            else:
                k += 1
        return count
        
         ####second solution
        g.sort()
        s.sort()
        i = 0
        count = 0
        for e in s:
            if i == len(g):
                break
            if g[i] <= e:
                count += 1
                i += 1
        return count
