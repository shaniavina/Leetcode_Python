class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if len(prices) == 0:
            return profit
        for i in range(len(prices) - 1):
            profit += max(0, prices[i+1] - prices[i])
        return profit
        
if __name__ == '__main__':
    print Solution().maxProfit([1,4,2,5,2,6,3,7,8,9])
