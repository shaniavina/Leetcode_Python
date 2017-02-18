class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == num:
                    res.append('%d:%02d' % (h, m))
        return res
                
               ###second solution
             ans = []
        for x in range(1024):
            if bin(x).count('1') == num:
                h, m = x >> 6, x & 0x3F               ##?????????????
                if h < 12 and m < 60:
                    ans.append('%d:%02d' % (h, m))
        return ans
