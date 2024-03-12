"""
Problem Link: https://leetcode.com/problems/longest-palindromic-substring/description/
Topics: Dynamic programming, string

[DEF] A string is palindromic if it reads the same forward and backward.
[DEF] A substring is a contiguous non-empty sequence of characters within a string.

Given a string s return the longest 

Brute Force Solution: 
[1] Caculate the length of every possible substring & check if its palindromic. (O(n^2) time complexity)
[2] Check the center of substring and work our way outwards, checking at each step to see if the characters match. 
    - Each check runs in O(n) time
    - Must do this for each substring generated -> O(n^2) time
        - Brute force: O(n^3) time!

Improved O(n^2) Solution:
    Key point: We can check ALL substrings with the SAME center in a single pass
    Visiting every center: O(n), checking palindrome O(n) -> Overall O(n^2) time complexity.

"""

class Solution:
    def longestPalindrome_bruteforce(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        def isPalindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        longest_palindrome = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if isPalindrome(sub) and len(sub) > len(longest_palindrome):
                    longest_palindrome = sub
        return longest_palindrome


    def longestPalindrome(self, s: str) -> str:
        def expand(l, r): # center of the indices
            while l >=0 and r < len(s) and s[r] == s[l]:
                r += 1
                l -= 1
            return s[l+1:r] # return the chars inside the bound

        result = ""
        for i in range(len(s)):
            sub1 = expand(i, i)
            if len(sub1) > len(result):
                result = sub1
            sub2 = expand(i, i+1)
            if len(sub2) > len(result):
                result = sub2
        return result




sol = Solution()
s = "babad"
print(sol.longestPalindrome_bruteforce(s)) # O(n^3) time complexity
print(sol.longestPalindrome(s)) # O(n^2) time complexity

