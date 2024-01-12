"""
Problem Link: https://leetcode.com/problems/is-subsequence/description/

"""

class Solution:
    # Runtime: Beats 70.47% of users with Python3
    # Memory: Beats 14.50% of users with Python3
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        num_remaining_s = len(s)
        pos = 0

        for ch in range(len(t)):
            if t[ch] == s[pos]:
                pos += 1
                num_remaining_s -= 1
            if num_remaining_s == 0:
                return True
        return False
    

    # Runtime: Beats 46.74% of users with Python3
    # Memory: Beats 14.50% of users with Python3
    def isSubsequence_simple(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
    
