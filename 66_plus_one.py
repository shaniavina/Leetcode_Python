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
            
            
           
##### second
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 1 and digits[0] == 9:
            return [1, 0]
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])
        return digits
