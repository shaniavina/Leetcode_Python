class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        def reverse(s, begin, end):
            for i in range((end - begin)/2):
                s[begin + i], s[end - 1 - i] = s[end - 1 - i], s[begin + i]
        
        s, i = list(s), 0
        for j in range(len(s) + 1):
            if j == len(s) or s[j] == ' ':
                reverse(s, i, j)
                i = j + 1
        return ''.join(s)
    
    
    #####second
    class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])[::-1]
        
