class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in reversed(range(len(digits))):
            digits[i] += carry
            carry = digits[i] / 10
            digits[i] %= 10
        if carry:
            digits = [1] + digits
        return digits

    
