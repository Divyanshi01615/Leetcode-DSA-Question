class Solution(object):
    def maxProfit(self, prices):
        buy=prices[0]
        profit=0
        for i in range(0,len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            sell=prices[i]-buy
            if sell>profit:
                profit=sell
        return profit
            

       
        