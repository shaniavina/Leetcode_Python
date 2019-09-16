class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        sum = a ^ b
        carry = (a & b) << 1
        sum += carry
        return sum
