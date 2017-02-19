class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        if not num:
            return '0'
        res = []
        while num and len(res) != 8:
            h = num & 15 ########hexadecimal
            if h < 10:
                res.append(chr(ord('0') + h))
            else:
                res.append(chr(ord('a') + h - 10))
            num >>= 4     ######num >> 4????
        res.reverse()
        return ''.join(res)
