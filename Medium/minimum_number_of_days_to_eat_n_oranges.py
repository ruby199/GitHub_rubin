# Leetcode 1553. Minimum Number of Days to Eat N Oranges

class Solution:
    def minDays(self, n: int) -> int:
        # Initialize dictionary with base cases: 
        # 0 oranges take 0 days, and 1 orange takes 1 day
        dp = { 0 : 0, 1: 1} 

        def dfs(n):
            # If the value for n oranges has been computed, return it (Memoization)
            if n in dp:
                return dp[n]
            
            # Calculate days if we eat half the oranges:
            # 1 for current day, n%2 days for remaining (if n is odd), 
            # and recursive call for half of the oranges
            one = 1 + (n % 2) + dfs(n // 2) 
            
            # Calculate days if we eat two-thirds of the oranges:
            # 1 for current day, n%3 days for the oranges remaining after eating 2n/3 oranges
            # and recursive call for one-third of the oranges
            two = 1 + (n % 3) + dfs(n // 3)
            
            # Store the minimum number of days between the two methods in the dp dictionary
            dp[n] = min(one, two) 
            
            return dp[n]
        
        # Return the minimum days required for n oranges
        return dfs(n)
