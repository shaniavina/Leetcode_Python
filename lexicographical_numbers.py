class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        high = 1
        while high * 10 <= n:
            high *= 10
        higher = high * 10
        withkeys = []
        for i in range(1, n + 1):
            key = i
            while key < high:
                key *= 10
            withkeys.append(key * higher + i)
        withkeys.sort()
        return [ki % higher for ki in withkeys]
