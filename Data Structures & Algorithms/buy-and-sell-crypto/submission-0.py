class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minprice = prices[0]
        for p in prices[1:]:
            profit = max(profit, p-minprice)
            minprice = min(minprice, p)

        return profit    
        