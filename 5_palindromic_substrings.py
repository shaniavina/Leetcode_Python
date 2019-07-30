class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return ''
        maxLen, start = 1, 0
        for i in range(1, len(s)):
            if i - maxLen >= 1 and s[i - maxLen - 1: i + 1] == s[i - maxLen - 1: i + 1][::-1]:
                start = i - maxLen - 1
                maxLen += 2
            if i - maxLen >= 0 and s[i - maxLen: i + 1] == s[i - maxLen: i + 1][::-1]:
                start = i - maxLen
                maxLen += 1
        return s[start: start + maxLen]
        
        ####Manacher's Algorithm
        t = '#'.join('^{}$'.format(s))
        n = len(t)
        p = [0] * n
        center = radius = 0
        for i in range (1, n - 1):
            if radius > i:
                p[i] = min(radius - i, p[2*center - i]) 
            # Attempt to expand palindrome centered at i
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + p[i] > radius:
                center, radius = i, i + p[i]
                
        return sum((v + 1) / 2 for v in p)
                
            
        
