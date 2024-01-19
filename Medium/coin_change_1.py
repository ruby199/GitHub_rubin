"""
Problem Link: https://leetcode.com/problems/coin-change/description/

Brute force solution: calculate every combination of coins using recursion
# Time Complexity: O(n^m), where n is the number of coins, m is the amount. (inefficient)

- For each coin: remaining amount = total amount - coin value
- If the remaining amount is still greater than 0:
    - must find the fewest number of coins to make up the remaining amount. 
    - recursively call the same function again with the remaining amount. 

Dynamic Programming (Bottom-up approach):
- initialize an array of length amount, then fill each position the min num of coins.
# Time Complexity: O(m*n), where m is the amount and n is the number of coins.
# Memory: O(m) due to the array size m+1
  
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the DP array with 'infinity' for all amounts except for 0
        dp = [0] + ([float('inf')] * amount)

        # Iterate over each amount from 1 to the amount
        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        # If the last element is still infinity, the amount cannot be formed using the coins
        if dp[-1] == float('inf'):
            return -1 
        return dp[-1]
