class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_int = 2**31 - 1
        s = str(n)
        for i in range(len(s) - 1, 0, -1):
            if s[i] > s[i - 1]:
                for j in range(len(s) - 1, i - 1, -1):
                    if s[j] > s[i - 1]:
                        break
                new_s = s[:i-1] + s[j] + ''.join(sorted(s[i - 1:j] + s[j + 1:]))
                res = int(new_s)
                return res if res <= max_int else -1   ####-1 if overflow
        return -1    ###if doesnt exist
