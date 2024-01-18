"""
Problem Link: https://leetcode.com/problems/climbing-stairs/description/?envType=daily-question&envId=2024-01-18

Approach 1. Recursive Approch.
- Time Complexity: O(2^n) time
- Time Limit Exceeded

Approach 2. Bottom-up Dynamic programming approach
- Time Complexity: O(n) time
- Memory Complexity: O(n) for array

Approach 2. Bottom-up Dynamic programming approach without array
- Time Complexity: O(n) time
- Memory Complexity: O(1)

"""


class Solution:
    # Recursive Approach: Time Limit Exceeded
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    
    # Runtime: Beats 22.53% of users with Python3
    # Memory: Beats 50.44% of users with Python3
    def climbStairs_dynamic_arry(self, n: int) -> int:
        ways = [1] * (n + 1)
    
        for i in range(2, n + 1):
            prev1 = ways[i-1]
            prev2 = ways[i-2]
            ways[i] = prev1 + prev2

        return ways[n]

    # Runtime: Beats 91.43% of users with Python3
    # Memory: Beats 15.77% of users with Python3
    def climbStairs_dynamic(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        prev1 = 1
        prev2 = 1

        for i in range(n - 1):
            print(prev1, prev2, i)
            temp = prev2
            prev2 = temp + prev1
            prev1 = temp
    
        return prev2



print(Solution().climbStairs_dynamic(5))