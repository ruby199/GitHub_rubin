# Import the necessary module
from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}  # Dictionary to store the maximum total for subarray piles[l:r]

        # Helper function to calculate the maximum total
        def dfs(l, r):
            if l > r:
                return 0  # Base case: No elements to choose from
            if (l, r) in dp:
                return dp[(l, r)]  # Return the previously computed result if available

            # Determine whether it's Alice's turn to choose
            even = (r - l) % 2 == 0
            left = piles[l] if even else 0  # Alice chooses the left element if it's her turn
            right = piles[r] if even else 0  # Alice chooses the right element if it's her turn

            # Calculate the maximum total by considering both choices for Alice
            dp[(l, r)] = max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)

            return dp[(l, r)]  # Return the maximum total for the subarray

        # Start the recursive function with the entire array
        return dfs(0, len(piles) - 1) > 0  # Check if Alice's maximum total is greater than Bob's
    

# Example usage:
if __name__ == "__main__":
    solution = Solution()

    # Example: Alice can win
    piles1 = [3, 9, 1, 2]
    result1 = solution.stoneGame(piles1)
    print(f"Example 1: Can Alice win the game? {result1}")
