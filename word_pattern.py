class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(words) != len(pattern):
            return False
        
        pattern_map, words_map = {}, {}
        for i in range(len(words)):
            if pattern_map.get(pattern[i], -1) != words_map.get(words[i], -1):   #####if none, then the value is -1
                return False
            pattern_map[pattern[i]] = i
            words_map[words[i]] = i
        return True

    ######second
   
        words = str.split()
        if len(words) != len(pattern):
            return False
        
        map1 = {}
        map2 = {}     ####contradict: "abba""dog dog dog dog"
        for i in range(len(pattern)):
            if pattern[i] in map1:
                if map1[pattern[i]] != words[i]:
                    return False
            else:
                map1[pattern[i]] = words[i]
            if words[i] in map2:
                if map2[words[i]] != pattern[i]:
                    return False
            else:
                map2[words[i]] = pattern[i]    
                
                
                
        return True
            
        
