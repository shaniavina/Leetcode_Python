class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy, sell, coolDown = [0] * 2, [0] * 2, [0] * 2
        buy[0] = -prices[0]
        for i in range(1, len(prices)):
            ##buy today or bought before
            buy[i % 2] = max(coolDown[(i - 1) % 2] - prices[i], buy[(i - 1) % 2])
            ###sell today
            sell[i % 2] = prices[i] + buy[(i - 1) % 2]
            ####sold yesterday or before yesterday
            coolDown[i % 2] = max(coolDown[(i - 1) % 2], sell[(i - 1) % 2])
        return max(coolDown[(len(prices) - 1) % 2], sell[(len(prices) - 1) % 2])
