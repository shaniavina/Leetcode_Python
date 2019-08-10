class Solution(object):
    
    def quickSolver(self,prices):
        sum = 0
        for i in range(1, len(prices)):
            sum += max(0, prices[i] - prices[i - 1])
        return sum
        
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0 or len(prices) < 2:
            return 0
        
        #if k>= n/2, then it can't complete k transactions. The problem becomes buy-and-sell problem 2
        if k > len(prices) / 2:
            return self.quickSolver(prices)
        
        loc = [0 for i in range(k + 1)]
        glo = [0 for i in range(k + 1)]
        
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            for j in range(k, 0 ,-1):
                #if cur_profit <0, then the current transaction loses money, else, it can be max_global[i-1][j-1] + cur_profit,
                #or CANCEL the last day transaction and moves to the current transaction. 
                
                #loc[i][j] = max(glo[i - 1][j - 1] + max(0, diff), loc[i - 1][j] + diff)
                loc[j] = max(glo[j - 1] + max(0, diff), loc[j] + diff)
                #glo[i][j] = max(glo[i - 1][j], loc[i][j])
                glo[j] = max(glo[j], loc[j])
        return glo[k]

    
    #Time complexity, O(nk)
    #Space complexity, O(nk)
    
    
