class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        for i in range(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])
        return profit
        
if __name__ == '__main__':
    print Solution().maxProfit([1,4,2,5,2,6,3,7,8,9])
