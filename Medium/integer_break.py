class Solution:
    def integerBreak(self, n: int) -> int:
        # Initialize a dictionary for dynamic programming (DP) with base case
        dp = {1: 1}

        # Iteratively compute the maximum product for each number from 2 to n
        for num in range(2, n + 1):
            # Set initial value for dp[num]; it's zero if num equals n, otherwise num
            dp[num] = 0 if num == n else num

            # Try breaking the number into two parts and calculate their product
            for i in range(1, num):
                # Calculate product of the two parts
                val = dp[i] * dp[num - i]
                # Update dp[num] if we find a larger product
                dp[num] = max(dp[num], val)

        # Return the maximum product for n
        return dp[n]

        # Define a recursive function for depth-first search (DFS)
        def dfs(num):
            # Return the stored value if already computed
            if num in dp:
                return dp[num]
            
            # Initialize dp[num] for the current number
            dp[num] = 0 if num == n else num
            
            # Try different splits and recursively compute their products
            for i in range(1, num):
                # Calculate product of the two parts using DFS
                val = dfs(i) * dfs(num - i)
                # Update dp[num] if a larger product is found
                dp[num] = max(dp[num], val)
            
            # Return the computed value for num
            return dp[num]
        
        # Start DFS from the given number n
        return dfs(n)
