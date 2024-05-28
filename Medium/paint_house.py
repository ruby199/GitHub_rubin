"""
Problem Link: https://leetcode.com/problems/paint-house/description/

There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. 
The cost of painting each house with a certain color is different. 
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...

Return the minimum cost to paint all houses.

"""

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # Edge case
        if not costs:
            return 0

        memo = {}
        
        # Define the recursive function with memoization
        def dp(i, color):
            # If we've reached the last house, return 0 as there's no cost to add
            if i == len(costs):
                return 0
            
            # If result is already computed, return it from the memo
            if (i, color) in memo:
                return memo[(i, color)]
            
            total_cost = float('inf')
            # Check the cost for the current house's color choice
            for next_color in range(3):
                if next_color != color:
                    current_cost = costs[i][color] + dp(i + 1, next_color)
                    total_cost = min(total_cost, current_cost)
            
            # Memoize
            memo[(i, color)] = total_cost
            return total_cost
        
        # Calculate the minimum cost starting from the first house,  each color
        return min(dp(0, 0), dp(0, 1), dp(0, 2))