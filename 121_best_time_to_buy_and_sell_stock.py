class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        maxProfit, minPrice = 0, float('inf')
        for n in prices:
            minPrice = min(minPrice, n)
            maxProfit = max(maxProfit, n - minPrice)
        return maxProfit
            
