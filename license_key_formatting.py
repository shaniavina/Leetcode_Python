class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = []
        for i in reversed(range(len(S))):
            if S[i] == '-':
                continue
            if len(res) % (K + 1) == K:
                res += '-'
            res += S[i].upper()
        return ''.join(reversed(res))
