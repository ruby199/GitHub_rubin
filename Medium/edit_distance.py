"""
Problem Link: https://leetcode.com/problems/edit-distance/description/

Topics: String, Dynamic Programming
"""

from collections import deque


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize the DP table for transformations involving the empty string
        for i in range(m + 1):
            dp[i][0] = i # Requires i deletions to transform word1[0:i] to ""
        for j in range(n + 1):
            dp[0][j] = j # Requires j insetions to transform "" to word[0:j]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] # No operation needed if characters match
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1, # Deletion
                        dp[i][j - 1] + 1, # Insertion
                        dp[i - 1][j - 1] + 1 # Substitution
                    )
        return dp[m][n]

    def minDistanceBottomUp(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        cache = [[float("inf")] * (n + 1) for _ in range(m + 1)]

        # Base cases: converting to/from empty strings
        # for j in range(len(word2) + 1):
        #     cache[len(word1)][j] = len(word2) - j

        # for i in range(len(word2) + 1):
        #     cache[len(word2)][i] = len(word1) - i
        
        for i in range(m + 1):
            cache[i][n] = m - i  # Cost of deleting the remaining characters in word1 to match empty word2
        for j in range(n + 1):
            cache[m][j] = n - j  # Cost of adding the remaining characters in word2 to match empty word1

        # Filing the table from bottom right to top left
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) -1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1] # No operation is needed if the chars match
                else:
                    # consider 3 cases: delete, insert, replace
                    cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1])
        return cache[0][0]


# Test

word1 = 'horse'
word2 = 'ros'

sol = Solution()

print(sol.minDistance(word1, word2))
print(sol.minDistanceBottomUp(word1, word2))