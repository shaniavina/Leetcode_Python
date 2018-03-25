class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # ####there should be 2*n -1 center
        # n = len(s)
        # res = 0
        # for i in range(2 * n - 1):
        #     left = i / 2
        #     right = left + i % 2
        #     while left >= 0 and right < n and s[left] == s[right]:
        #         res += 1
        #         left -= 1
        #         right += 1
        # return res
        
       
        
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
                
            
        
