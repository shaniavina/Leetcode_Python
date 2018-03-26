class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        current_count = [0 for i in range(52)]
        expect_count = [0 for i in range(52)]
        for char in t:
            expect_count[ord(char) - ord('a')] += 1
        
        count, start, min_start, min_width = 0, 0, 0, float('inf')
        for i in range(len(s)):
            current_count[ord(s[i]) - ord('a')] += 1
            if current_count[ord(s[i]) - ord('a')] <= expect_count[ord(s[i]) - ord('a')]:
                count += 1
            if count == len(t):
                while expect_count[ord(s[start]) - ord('a')] == 0 or current_count[ord(s[start]) - ord('a')] > expect_count[ord(s[start]) - ord('a')]:
                    current_count[ord(s[start]) - ord('a')] -= 1
                    start += 1
                if min_width > i - start + 1:
                    min_width = i - start + 1
                    min_start = start
        if min_width == float('inf'):
            return ''
        return s[min_start:min_start + min_width]
