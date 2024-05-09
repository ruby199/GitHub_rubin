"""
Problem Link: https://leetcode.com/problems/palindrome-permutation-ii/description/

Description:
    Given a string s, return all the palindromic permutations (without duplicates) of it.
    You may return the answer in any order. If s has no palindromic permutation, return an empty list.

Topics: Hash Table(counter in python), String, Backtracking

Approach 1. Brute Fore [Time Limit Exceeded]
    - To generate every possible permutation of the given string sss and check if the generated permutation is a palindrome.
    - Time Complexity: O((n + 1)!)
    - Space Complexity: O(n)

Approach 2. Backtracking
    - key point: generate only the first half of the palindromic string and to append its reverse string to itself to generate the full length palindromic string.
    - Time Complexity: O((n/2 + 1)!)
    - Space Complexity: O(n)

"""

from typing import Counter


class Solution:
    def generatePalindromes1(self, s):
        # Time Limit Exceeded

        result = []

        def backtrack(comb, counter):
            # Base case
            # if len(comb) == len(s):
            if len(comb) == len(s) and comb == comb[::-1]:
                result.append("".join(comb))
                return
            
            for l in list(counter):
                if counter[l] > 0:
                    comb.append(l)
                    counter[l] -= 1
                    backtrack(comb, counter)
                    comb.pop()
                    counter[l] += 1
        
        backtrack([], Counter(s))

        # result = [item for item in result if item == item[::-1]]

        return result

    def generatePalindromes2(self, s):
        # Check if a palindromic permutation is possible for s
        counter = Counter(s)
        if not self.canPermutePalindrome(counter):
            return []
        
        #  Prepare by storing half of each character's occurrences
        half = []
        mid = None

        for char, count in counter.items():
            if count % 2 == 1:
                mid = char
            half.extend(char * (count // 2))
        half = list(half)
        result = set()

        # Generate permutations of the half string
        self.permute(half, 0, mid, result)
        return list(result)
        
    def canPermutePalindrome(self, counter):
        return sum(count % 2 for count in counter.values()) <= 1
        # odd_count = sum(1 for count in counter.values() if count % 2 != 0)
        # if odd_count > 1:
        #     return -1

    def permute(self, s, l, mid, result):
        if l == len(s):
            palindrome = ''.join(s) + (mid or '') + ''.join(s[::-1])
            result.add(palindrome)
        else:
            seen = set() # to avoid duplicates

            for i in range(l, len(s)):
                if s[i] not in seen:
                    self.swap(s, l, i)
                    self.permute(s, l + 1, mid, result)
                    self.swap(s, l, i)

    def swap(self, s, i, j):
        s[i], s[j] = s[j], s[i]






sol = Solution()
s = "aabb"
print(sol.generatePalindromes1(s)) # Time Limit Exceeded
print(sol.generatePalindromes2(s))
        