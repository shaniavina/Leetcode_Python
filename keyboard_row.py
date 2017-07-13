class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        # res = []
        # for word in words:
        #     w = set(word.lower())    ###w has to be a set()
        #     if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
        #         res.append(word)
        # return res
        
        
        ref = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        res = []
        k = 0
        for word in words:
            
            for i in range(len(ref)):
                if word[0].lower() in ref[i]:
                    k = i
                    break
            for w in word:
                if w.lower() not in ref[k]:
                    break
            else:     ########for else loop!!
                res.append(word)
        return res
                
                    
