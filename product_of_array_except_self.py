class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #The idea is simply. The product basically is calculated using the numbers before the current number and the numbers after the current number. Thus, we can scan the array twice. First, we calcuate the running product of the part before the current number. Second, we calculate the running product of the part after the current number through scanning from the end of the array.
        p = 1
        n = len(nums)
        res = []     ###[0] * n
        for i in range(n):
            res.append(p)
            p *= nums[i]
        p = 1
        for i in reversed(range(n)):
            res[i] *= p
            p *= nums[i]
        return res
        
        
    
