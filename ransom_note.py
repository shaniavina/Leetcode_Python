class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts = [0] *  26
        letters = 0
        
        for c in ransomNote:
            if counts[ord(c) - ord('a')] == 0:
                letters += 1
            counts[ord(c) - ord('a')] += 1
        for c in magazine:
            counts[ord(c) - ord('a')] -= 1
            if counts[ord(c) - ord('a')] == 0:
                letters -= 1
                if letters == 0:
                    break
        return letters == 0
            
            
Second:
    
    return not Counter(ransomNote) - Counter(magazine)
    
Third:
    cnt = collections.Counter(magazine)
        for letter in ransomNote:
            cnt[letter] -= 1
            if cnt[letter] <0: return False
        return True
##counter is a dictionary
