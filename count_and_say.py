class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = '1'
        for i in range(n - 1):
            seq = self.getNext(seq)   ####using a function and do it n times
        return seq
    def getNext(self, seq):
        i, next_seq = 0, ''
        while i < len(seq):
            cnt = 1
            while i < len(seq) - 1 and seq[i] == seq[i + 1]: ####len - 1
                cnt += 1
                i += 1
            next_seq += str(cnt) + seq[i]
            i += 1
        return next_seq
            
