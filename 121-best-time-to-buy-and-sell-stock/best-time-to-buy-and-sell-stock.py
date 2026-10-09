
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)

            current_profit = price - min_price
            max_profit = max(max_profit, current_profit)
        return max_profit
    
    # TC: O(N), where N is the size of the array
    # SC: O(1)