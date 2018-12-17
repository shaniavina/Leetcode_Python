class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1   
        for i in reversed(range(len(digits))):  #####reversed(range())
            carry += digits[i]
            digits[i] = carry % 10
            carry /= 10
        if carry:
            digits = [1] + digits  ####list add forward
        return digits
            
            
           
