"""
Probelm Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75

"""

from typing import Counter


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        max_vowel = 0
        current_count = 0

        # first window of size k
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
            
        max_vowel = current_count

        # size k sliding window
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current_count -= 1
            if s[i] in vowels:
                current_count += 1
                
            max_vowel = max(max_vowel, current_count)

        return max_vowel
    


             


sol = Solution()

s = "abciiidef"
k = 3
print(sol.maxVowels(s, k)) # Exected output: 3