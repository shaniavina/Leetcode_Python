class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            res += n % 2
            n /= 2
        return res


#####2
class Solution:
    # @param n, an integer                   ####Each time of "n &= n - 1", we delete one '1' from n.
    # @return an integer
    def hammingWeight(self, n):
        result = 0
        while n:
            n &= n - 1
            result += 1
        return result
