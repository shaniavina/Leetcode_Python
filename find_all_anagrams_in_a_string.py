class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        
        cnt = [0] * 26
        for c in p:
            cnt[ord(c) - ord('a')] += 1
        left, right = 0, 0                         #####left, right pointer
        while right < len(s):
            cnt[ord(s[right]) - ord('a')] -= 1
            while left <= right and cnt[ord(s[right]) - ord('a')] < 0:   #####while if!!
                cnt[ord(s[left]) - ord('a')] += 1
                left += 1
            if right - left + 1 == len(p):
                result.append(left)
            right += 1
        return result

    
