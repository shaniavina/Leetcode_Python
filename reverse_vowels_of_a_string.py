class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel_set = set(['a', 'e', 'i', 'o', 'u'])
        vowels = []
        vowel_pos = []
        str_list = []
        
        for i in range(len(s)):
            str_list.append(s[i])
            if s[i].lower() in vowel_set:
                vowels.append(s[i])
                vowel_pos.append(i)
                
        vowels.reverse()
        
        for i in range(len(vowels)):
            str_list[vowel_pos[i]] = vowels[i]
            
        return "".join(str_list)
        
        
        
