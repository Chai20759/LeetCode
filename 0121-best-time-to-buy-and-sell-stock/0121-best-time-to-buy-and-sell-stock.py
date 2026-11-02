class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price=prices[0]
        max_price=0

        for price in prices:
            if price<min_price:
                min_price=price
            
            profit=price-min_price

            if profit>max_price:
                max_price=profit
        return max_price
        