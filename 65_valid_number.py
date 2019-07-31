class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        start, end = 0, len(s) - 1
        if not s:
            return False
        if start < end and (s[start] == '+' or s[start] == '-'):
            start += 1
        num, dot, exp = False, False, False
        for i in range(start, len(s)):
            if s[i] >= '0' and s[i] <= '9':
                num = True
            elif s[i] == '.':
                if dot or exp:
                    return False
                dot = True
            elif s[i] == 'e' or s[i] == 'E':
                if exp or not num:
                    return False
                exp, num = True, False
            elif s[i] == '+' or s[i] == '-':
                if s[i - 1] != 'e':
                    return False
            else:
                return False
        return num
