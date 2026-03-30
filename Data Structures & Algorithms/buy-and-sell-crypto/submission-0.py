class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest = prices[0]
        profit = 0

        for x in prices:
            profit = max(profit, x - lowest)
            lowest = min(lowest, x)
        
        return profit

