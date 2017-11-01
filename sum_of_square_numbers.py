class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
#         def is_square(num):
#             return int(num ** 0.5) ** 2 == num
        
#         return any(is_square(c - i * i) for i in range(int(c ** 0.5) + 1))
        
    
    ###second: binary search
        maxi = 1
        while maxi ** 2 < c:
            maxi += 1

        low = 0
        high = maxi
        while low <= high:
            sumi = low ** 2 + high ** 2
            if sumi == c:
                return True
            elif sumi < c:
                low += 1
            else:
                high -= 1
        return False
