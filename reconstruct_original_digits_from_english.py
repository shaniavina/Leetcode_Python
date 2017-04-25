from collections import Counter
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnts = [Counter(_) for _ in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']]
        order = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        unique_char = ['z', 'o', 'w', 't', 'u', 'f', 'x', 's', 'g', 'n']
        
        cnt = Counter(s)
        res = []
        for i in order:
            while cnt[unique_char[i]] > 0:
                cnt -= cnts[i]
                res.append(i)
        res.sort()
        return ''.join(map(str,res))    #####res = [0,1,3]
