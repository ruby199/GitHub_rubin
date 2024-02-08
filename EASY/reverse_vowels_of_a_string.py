"""
Problem Description: https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

Solution: Use two pointers

Time Complexity: O(n)
Space Complexity: O(n)

"""

class Solution:
    def reverseVowels(self, s: str) -> str:

        s = list(s)
        
        vowels = "aeiouAEIOU"
        l, r = 0, len(s) - 1

        while l < r:
            if  s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                r  -= 1
                l += 1
            elif s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
                
        return "".join(s)

        