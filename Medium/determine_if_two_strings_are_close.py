"""
Problem Link: https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

Approach 1. Using Hash Map.

Time Complexity : O(n)
Space Complexity: O(1)
"""

from typing import Counter


class Solution:
    def closeStrings_hashmap(self, word1: str, word2: str) -> bool:
        # Count the frequency of each character in both words
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        # Check if both words have the same unique characters
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        
        # Check if both words have the same frequency distribution
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False
        
        return True




sol = Solution()
word1 = "abc"
word2 = "bca"
print(sol.closeStrings_hashmap(word1, word2))

