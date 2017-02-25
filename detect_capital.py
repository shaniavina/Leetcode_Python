
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 1:
            return True
        
        if ord(word[0]) < ord('a'):
            if ord(word[1]) < ord('a'):
                for i in range(2, len(word)):
                    if ord(word[i]) >= ord('a'):
                        return False
            else:
                for i in range(2, len(word)):
                    if ord(word[i]) < ord('a'):
                        return False
                
        else:
            for i in range(1, len(word)):
                if ord(word[i]) < ord('a'):
                    return False
        return True
        
        ############second solution

def detectCapitalUse(self, word):
    return word.isupper() or word.islower() or word.istitle()
