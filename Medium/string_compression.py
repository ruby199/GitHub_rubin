"""
Problem Link: https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75

"""

from typing import Counter


class Solution:
    def compress(self, chars) -> int:

        if not chars:
            return 0
        
        p1 = 0
        l = 0 # to keep track of the length of the compressed string

        while p1 < len(chars):
            char = chars[p1]
            count = 0
            # count the occurrences of the current character
            while p1 < len(chars) and chars[p1] == char:
                p1 += 1
                count += 1
            chars[l] = char
            l += 1
            if count > 1:
                for c in str(count):
                    chars[l] = c
                    l += 1
        return l

                





sol = Solution()
chars1 = ["a","a","b","b","c","c","c"]
print(sol.compress(chars1)) # expected output: 6

chars2 = ["c","c","b","a","a","a","a","a","a","a","a","a","a"]
print(sol.compress(chars2)) # expected output: 6