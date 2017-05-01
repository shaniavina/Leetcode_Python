class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        lst = []
        i = 1
        while i ** 2 <= n:
            lst.append(i ** 2)
            i += 1
        
        cnt = 0
        toCheck = {n}     #####build up as a set, you dont wanna check twice
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x - y)
                    
            toCheck = temp
            
        return cnt
