class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        #####symmetric, using pairs
        lookup = [('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]
        i, j = 0, len(num) - 1
        while i <= j:
            if (num[i], num[j]) not in lookup:
                return False
            i += 1
            j -= 1
        return True
            
