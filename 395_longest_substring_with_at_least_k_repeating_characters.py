from collections import Counter    

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        hashmap = Counter(s)
        hashset = set([ch for ch in hashmap if hashmap[ch] < k]) ## bad guys
        
        if not hashset:
            return len(s)
        start = 0
        intervals = []
        while start < len(s):
            ch = s[start]
            if ch not in hashset:
                end = start
                while end < len(s):
                    if s[end] not in hashset:
                        end += 1
                    else:
                        break
                intervals.append((start, end))
                start = end
            else:
                start += 1
        result = 0
        for i, j in intervals:
            result = max(result, self.longestSubstrings(s[i:j], k))
        return result
