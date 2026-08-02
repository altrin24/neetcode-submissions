class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = float('inf')
        for i in range(0,len(prices)-1):
            profit = 0
            buy = min(buy,prices[i])
            if (i+1) <= len(prices)-1:
                profit = prices[i+1] - buy
                maxProfit = max(profit,maxProfit)
            else:
                profit = prices[i] - buy
                maxProfit = max(profit,maxProfit)

        return maxProfit        


            







        