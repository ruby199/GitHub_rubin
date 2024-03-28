"""
Problem Link: https://leetcode.com/problems/partition-array-for-maximum-sum/description/

Topics: Array, Dynamic Programming

Bottom-up (Tabulation): Bottom-up is implemented with iteration and starts at the base cases. 
Top-down (Memoization): Top-down is implemented with recursion and made efficient with memoization.

"""


class Solution:
    def maxSumAfterPartitioning_top_down(self, arr, k: int) -> int:
        memo = {}
        
        def dp(i):
            # Base case
            if i == len(arr):
                return 0
            if i in memo:
                return memo[i]
            
            max_val = 0
            max_sum = 0

            # Iterate over all possible partition sizes up to k
            for j in range(1, min(k, len(arr) - i) + 1):
                max_val = max(max_val, arr[i + j - 1]) # update the max_val of the current partition
                current_sum = max_val * j + dp(i + j) # sum of the current partition
                max_sum = max(max_sum, current_sum) # update max_sum if cur_sum is larger
            
            memo[i] = max_sum
            return max_sum
        
        return dp(0)


    def maxSumAfterPartitioning_bottom_up(self, arr, k: int) -> int: # using tabulation
        n = len(arr)
        dp = [0] * (n + 1) # dp array to store max sums up to each index

        for i in range(1, n + 1):
            max_val = 0
            for j in range(1, min(k, i) + 1): # for each i look back up to k positions
                max_val = max(max_val, arr[i - j]) # find the max value within this window
                dp[i] = max(dp[i], dp[i - j] + max_val * j) # get the max sum using this partition -> update the db
        return dp[n]



sol = Solution()

arr = [1,15,7,9,2,5,10]
k = 3
print(sol.maxSumAfterPartitioning_top_down(arr, k)) # expected output: 84 # arr becomes [15,15,15,9,10,10,10]
print(sol.maxSumAfterPartitioning_bottom_up(arr, k)) # expected output: 84 # arr becomes [15,15,15,9,10,10,10]