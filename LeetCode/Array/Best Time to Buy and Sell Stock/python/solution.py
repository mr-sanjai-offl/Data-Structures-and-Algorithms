class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        profit = 0

        for i in range(1,len(prices)):
            sell = prices[i]
            if(buy<=sell):
                profit = max(profit,sell-buy)
            else:
                buy=sell
        return profit