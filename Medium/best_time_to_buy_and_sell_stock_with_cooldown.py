class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dynamic programming dictionary to store the maximum profit for a given state
        # Key: (current day, buying status), Value: maximum profit
        dp = {}

        def dfs(i, buying):
            # Base case: If the current day exceeds the length of the prices list, no more transactions can be made
            if i >= len(prices):
                return 0

            # Check if the current state has already been computed to avoid redundant calculations
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            # Decision making for the current state
            if buying:
                # If buying, two options: buy stock or cooldown
                # Buy: Buy stock on the current day and sell it later
                buy = dfs(i + 1, not buying) - prices[i]
                # Cooldown: Skip the current day without buying
                cooldown = dfs(i + 1, buying)
                # Store the maximum profit from the two options in dp
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # If selling, two options: sell stock or cooldown
                # Sell: Sell stock on the current day and add its price to the profit
                sell = dfs(i + 2, not buying) + prices[i]  # Include cooldown day after selling
                # Cooldown: Skip the current day without selling
                cooldown = dfs(i + 1, buying)
                # Store the maximum profit from the two options in dp
                dp[(i, buying)] = max(sell, cooldown)
            
            # Return the maximum profit for the current state
            return dp[(i, buying)]

        # Start the search from day 0 with the intent to buy
        return dfs(0, True)


        



def test_maxProfit():
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 2, 3, 0, 2], 3),  # Test case 1
        ([1], 0),             # Test case 2
        # Add more test cases here
    ]

    for i, (prices, expected) in enumerate(test_cases):
        result = solution.maxProfit(prices)
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed.")

# Call the test function
test_maxProfit()