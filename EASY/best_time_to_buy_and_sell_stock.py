"""
Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
Advanced Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/?envType=study-plan-v2&envId=leetcode-75

# Google Interview question
* Problem: Remember we need to buy low and sell high!

[1] Brute Force Solution: Calculate every combination

Key insight:
- If buying price is higher than the selling price, there is no point calculating the profit. 

[2] greedy algorithm

[3] 2 pointers approach 

Time Complexity: O(n)
Only n-1 comparison is needed.


"""

class Solution:
    def maxProfit(self, prices) -> int: # greedy algorithm
        buy = prices[0] # min val
        profit = 0

        for sell in prices[1:]:
            if sell > buy: # if profit is positive
                profit = max(profit, sell - buy)
            else:
                buy = sell
        return profit

    def maxProfix_two_pointers(self, prices) -> int:
        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r # instead of l+=1 since we want the left to go the the next smallest value. 
            r += 1

        return profit


prices = [7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfix_two_pointers(prices))
