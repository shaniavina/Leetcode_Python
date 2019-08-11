class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ##buy[i] = max(sell[i-2]-price, buy[i-1])
        ##sell[i] = max(buy[i-1]+price, sell[i-1])
        if len(prices) < 2:
            return 0
        sell, buy, pre_sell, pre_buy = 0, -prices[0], 0, 0
        for p in prices:
            pre_buy = buy
            buy = max(pre_sell - p, pre_buy)
            pre_sell = sell
            sell = max(pre_buy + p, pre_sell)
        return sell
