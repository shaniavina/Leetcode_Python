class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if not b:
            return 1
        return pow(a, b.pop(), 1337) * self.superPow(pow(a, 10, 1337), b) % 1337
        
        
        
        ####n1*n2 % 1337 == (n1 % 1337)*(n2 % 1337) % 1337
####If b = m*10 + d, we have a**b == (a**d)*(a**10)**m
