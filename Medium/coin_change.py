class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # max value as default value
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins: # go through every coin
                if a - c >= 0: # continue to search if not negative
                    dp[a] = min(dp[a], 1 + dp[a - c]) # 1 comes from the coin we are using. 

        return dp[amount] if dp[amount] != amount + 1 else -1
