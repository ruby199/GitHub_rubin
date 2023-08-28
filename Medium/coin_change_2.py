class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # # Method 1. Dynamic programming (2D Table)
        # # This method uses 2-D table to represent the # of combinations to make up amounts using up to 'i' coins.
        # dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        # dp[0] = [1] * (len(coins) + 1)

        # for a in range(1, amount + 1):
        #     for i in range(len(coins) -1, -1, -1):
        #         # if current amount - coins[i] is non-negative, it means the coin can be used to contribute to the current amount.
        #         # Combinations without using the current coin:
        #         dp[a][i] = dp[a][i + 1]
        #         if a - coins[i] >= 0: 
        #             # combination using the current coin.
        #             dp[a][i] += dp[a - coins[i]][i]
        # return dp[amount][0]

        # Method 2. Depth first search with memoization (recursive approach to calculate the number of combinations.)
        # cache = {}

        # def dfs(i, a):
        #     if a == amount:
        #         return 1
        #     if a > amount:
        #         return 0
        #     if i == len(coins):
        #         return 0
        #     if (i, a) in cache:
        #         return cache[(i, a)]
            
        #     cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a) # using current coin & skipping the current coin
        #     return cache[(i, a)]
        
        # return dfs(0, 0)

        # Method 3. Dynamic programming (1D Table with Temp Array) - simple 1D array

        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1) # temp nextDP array to store the updated number of comb for each amount using this coin.
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0: # if curr amount - coin's value is non-negative -> update the temp nextDP array. 
                    nextDP[a] += nextDP[a - coins[i]] # dp[a]: comb without using current coin, # nextDP[a-coins[i]] using current coin. 
            dp = nextDP # After updating all amounts with current coin.
        return dp[amount]
