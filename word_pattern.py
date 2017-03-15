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
