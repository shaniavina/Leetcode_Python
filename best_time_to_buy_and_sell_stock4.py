class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        #Time complexity, O(nk)
    #Space complexity, O(nk)
        if len(prices) < 2:
            return 0
        
        max_profit = 0
        #if k>= n/2, then it can't complete k transactions. The problem becomes buy-and-sell problem 2
        if k >= len(prices) / 2:
            for i in range(1, len(prices)):
                max_profit += max(0, prices[i] - prices[i - 1])
            return max_profit
        #max_global[i][j] is to store the maximum profit, at day j, and having i transactions already
    #max_local[i][j] is to store the maximum profit at day j, having i transactions already, and having transaction at day j
        global_max = [[0 for j in range(len(prices))] for i in range(k + 1)]
        local_max = [[0 for j in range(len(prices))] for i in range(k + 1)]
        
        for j in range(1, len(prices)):
            cur_profit = prices[j] - prices[j - 1]
            for i in range(1, k + 1):
                #if cur_profit <0, then the current transaction loses money, else, it can be max_global[i-1][j-1] + cur_profit,
                #or CANCEL the last day transaction and moves to the current transaction. 
                local_max[i][j] = max(global_max[i - 1][j - 1] + max(0, cur_profit), local_max[i][j - 1] + cur_profit)
                #This is more obvious, by looking at whether transaction on day j has influenced max_global or not.
                global_max[i][j] = max(global_max[i][j - 1], local_max[i][j])
        return global_max[k][-1]
        
