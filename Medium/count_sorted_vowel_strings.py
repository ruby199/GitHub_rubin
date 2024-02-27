"""
Problem Link: https://leetcode.com/problems/count-sorted-vowel-strings/description/

[1] Recursive Solution

- Time Complexity: O(n^4)
- Space Complexity: O(n)


[2] (more optimized) Direct Mathematical solution

- Time Complexity: O(1)
- Space Complexity: O(1)

* Extra Resources:
- Combinations & Permutations:    https://www.mathsisfun.com/combinatorics/combinations-permutations.html

"""


class Solution:
    def countVowelStrings_rec(self, n: int) -> int:
        # Memory: Beats 89.86% of users with Python3
        # Time: Beats 15.67% of users with Python3

        def rec(n, k): # n: remaining length, k: starting index of vowel to consider for appending
            if n == 0: # we've entered all values
                return 1

            total = 0

            for i in range(k, 5):
                total += rec(n-1, i)
            
            return total
        
        return rec(n, 0)


    def countVowelStrings(self, n: int) -> int:
        # Memory: Beats 50.41% of users with Python3
        # Time: Beats 40.16% of users with Python3

        # C(n+k−1,k) = (n+k-1)! / (n!(k-1)!) = (n+4)! / (n!4!) = ((n+4) * (n+3) * (n+2) * (n+1)) // 24
        return ((n+4) * (n+3) * (n+2) * (n+1)) // 24

sol = Solution()
print(sol.countVowelStrings(33))