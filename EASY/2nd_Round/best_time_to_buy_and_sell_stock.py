"""
Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Topics: Array, Dynamic Programming

"""

class Solution:
    def maxProfit(self, prices) -> int:
        """
        Runtime: Beats 15.46 %
        Memory: Beats 90.88 %
        """
        if not prices:
            return 0

        max_profit = 0
        min_price = prices[0]

        for r in range(1, len(prices)):
            profit = prices[r] - min_price
            max_profit = max(max_profit, profit)
            
            min_price = min(min_price, prices[r])
        return max_profit

    def maxProfit_2(self, prices) -> int:
        """
        Runtime: Beats 57.81 %
        Memory: Beats 90.88 %
        """
        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return profit
            


prices = [7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(prices)) # Expected output: 5
print(sol.maxProfit_2(prices)) # Expected output: 5