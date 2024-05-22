"""
Problem Link: https://leetcode.com/problems/palindrome-partitioning/description/?envType=daily-question&envId=2024-05-22

Given a string s, partition s such that every  substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
 

Topics: String, Dynamic Programming, Backtracking
"""
class Solution:
    def partition(self, s: str):
        if not s:
            return []

        res = []
        part = []

        def dfs(i):
            def checkPalindrome(s, l, r):
                while l < r:
                    if s[l] != s[r]:
                        return False
                    l, r = l + 1, r - 1
                return True
            
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if checkPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res
        








sol = Solution()
s = "aab"
print(sol.partition(s)) # Expected Output: [["a","a","b"],["aa","b"]]