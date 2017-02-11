class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        res = []
        for word in words:
            w = set(word.lower())
            if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
                res.append(word)
        return res
        
         #second solution
        return [word for word in words if any(set(word.lower()) <= set(line) for line in ('qwertyuiop', 'asdfghjkl', 'zxcvbnm'))]
