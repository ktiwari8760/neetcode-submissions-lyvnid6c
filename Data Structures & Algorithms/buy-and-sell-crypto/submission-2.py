class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for sell in prices:
            if sell < buy:
                buy = sell
            else:
                profit = sell - buy
                max_profit = max(max_profit , profit)
        return max_profit