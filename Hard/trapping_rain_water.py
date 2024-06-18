"""
Problem Link: https://leetcode.com/problems/trapping-rain-water/description/

1. Brute Force
- For every bar, calculate the amount of water that can be trapped above it.
--> should try to find shorter of the tallest barts to its left and right

2. Dynamic Programming

"""

class Solution:
    def trap(self, height) -> int:
        ans = 0
        size = len(height)
        for i in range(1, size - 1):
            left_max = 0
            right_max = 0

            # maximum height of a bar found to the left of the current bar
            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])
            
            # maximum height of a bar found to the right of the current bar
            for j in range(i, size):
                right_max = max(right_max, height[j])
            
            ans += min(left_max, right_max) - height[i]
        return ans

    def trap_dp(self, height) -> int:
        if not height:
            return 0
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        ans = 0

        # Fill the left_max array
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        
        # Fill the right_max array
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        # Calculate the trapped water using the precomputed max arrays
        for i in range(n):
            ans += min(left_max[i], right_max[i]) - height[i]
        
        return ans




sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(height)) # Expected Output: 6
print(sol.trap_dp(height)) # Expected Output: 6