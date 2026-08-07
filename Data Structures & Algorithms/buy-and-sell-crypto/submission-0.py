class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        best_price = prices[0]
        for i in prices:
            if i<best_price:
                best_price=i
            if i-best_price>0 and i-best_price>max_profit:
                max_profit = i-best_price

        return max_profit
