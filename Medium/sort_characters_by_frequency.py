"""
Problem Link: https://leetcode.com/problems/sort-characters-by-frequency/?envType=daily-question&envId=2024-02-07

"""

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the freq of each character in the string
        count = Counter(s)
        
        # use sort function to sort the characters by frequency
        sorted_chars = sorted(count, key=lambda x: (-count[x], x))

        # Build the result string
        res = "".join(char * count[char] for char in sorted_chars)

        return res






sol = Solution()

s = "Tree"
print(sol.frequencySort(s))
