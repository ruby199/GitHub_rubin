class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i >= len(days):  # If we're past the last day, cost is zero
                return 0
            if i in dp:  # If we already know the answer, return it
                return dp[i]

            dp[i] = float("inf")  # Initialize to "infinite" cost

            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:  # Find the furthest day we can go with this ticket
                    j += 1
                dp[i] = min(dp[i], c + dfs(j))  # Take the minimum of existing cost and the cost if we buy this ticket

            return dp[i]

        return dfs(0)