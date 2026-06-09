class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minval = prices[0]
        profit = 0
        for i in prices:
            if i < minval:
                minval = i
            profit = max(profit, i-minval)
        
        return profit