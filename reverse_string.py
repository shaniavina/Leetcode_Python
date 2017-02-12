class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = [0] * (len(s))
        j = len(s)
        for i in range(len(s)):
            j -= 1
            res[j] = s[i]
            
        return "".join(res)
    
    
 ##solution 2
        return s[::-1]
