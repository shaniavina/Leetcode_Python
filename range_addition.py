# Time:  O(k + n)
# Space: O(1)

class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * length
        for up in updates:
            res[up[0]] += up[2]
            if up[1] + 1 < length:
                res[up[1] + 1] -= up[2]
        
        for i in range(1, length):
            res[i] += res[i - 1]
        return res
        
