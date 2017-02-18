class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit, min_price = 0, float("inf")
        for price in prices:
            min_price = min(min_price, price)
            maxProfit = max(maxProfit, price - min_price)
        return maxProfit
if __name__ == '__main__':
    print Solution().maxProfit([2,3,1,4,56,3,2])
