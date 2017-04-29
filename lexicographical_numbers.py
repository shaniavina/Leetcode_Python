class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        highdigit = 1
        while highdigit * 10 <= n:
            highdigit *= 10
        higherdigit = highdigit * 10
        withkeys = []
        for i in range(1, n + 1):
            key = i
            while key < highdigit:
                key *= 10
            withkeys.append(key * higherdigit + i)
        withkeys.sort()
        return [ki % higherdigit for ki in withkeys]
