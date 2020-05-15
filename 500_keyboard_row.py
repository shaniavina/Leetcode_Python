class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        """
        line_1 = ['q','w','e','r','t','y','u','i','o', 'p']
        line_2 = ['a','s','d','f','g','h','j','k','l']
        line_3 = ['z','x','c','v','b','n','m']
        res = []
        def in_one_line(word):
            if not word:
                return
            else:
                if word[0] in line_1:
                    pool = line_1
                elif word[0] in line_2:
                    pool = line_2
                else:
                    pool = line_3
            for c in word:
                if c not in pool:
                    return False
            return True
        
        for word in words:
            lower_word = word.lower()
            if in_one_line(lower_word) == True:
                res.append(word)
        return res
        """
        
        # solution 2
        row1 = set('QWERTYUIOP')
        row2 = set('ASDFGHJKL')
        row3 = set('ZXCVBNM')
        
        wordList = []
		
        for word in words:
			string = set(word.upper())
			for charSet in [row1, row2, row3]:
				if string & charSet == string:
					wordList.append(word)
					
        return wordList
        
