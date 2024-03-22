"""
Problem Link: https://leetcode.com/problems/divisor-game/submissions/1209622630/

Divisor Game
"""


class Solution:
    def divisorGame(self, n: int) -> bool:
        is_bob_turn = False

        while n > 1:
            found_move = False

            for x in range(1, n):
                if n % x == 0:
                    n -= x
                    found_move = True
                    break
            if not found_move:
                break
            
            is_bob_turn = not is_bob_turn

        return is_bob_turn
    

    def divisorGame_dp(self, n: int) -> bool:
        dp = [False] * (n + 1)

        # Base case:
        dp[0] = False

        if n > 0:
            dp[1] = False
        
        for i in range(2, n + 1):
            for x in range(1, i):
                if i % x == 0 and not dp[i - x]:
                    dp[i] = True
                    break
        return dp[n]
    

# Example usage:
sol = Solution()
n = 4
print(sol.divisorGame(n))  # Expected output: True
print(sol.divisorGame_dp(n))  # Expected output: True