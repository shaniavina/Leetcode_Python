# Time:  O(n * d), n is length of string, d is size of dictionary
# Space: O(d)
import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        dist, cur, visited, lookup = 0, [beginWord], set([beginWord]), set(wordList)
        while cur:
            next_q = []
            for word in cur:
                if word == endWord:
                    return dist + 1
                for i in range(len(word)):
                    for char in string.ascii_lowercase:
                        temp = word[:i] + char + word[i + 1 :]
                        if temp not in visited and temp in lookup:
                            visited.add(temp)
                            next_q.append(temp)
            dist += 1
            cur = next_q
        return 0
            
                
         
        
        
        
