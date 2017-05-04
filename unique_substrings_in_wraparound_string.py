class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        letters = [0] * 26
        result, length = 0, 0
        for i in range(len(p)):
            cur = ord(p[i]) - ord('a')
            if i > 0 and ord(p[i - 1]) != (cur - 1) % 26 + ord('a'):
                length = 0
            length += 1
            if length > letters[cur]:
                result += length - letters[cur]
                letters[cur] = length
        return result
            
