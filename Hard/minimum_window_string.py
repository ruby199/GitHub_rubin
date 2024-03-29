"""
Problem Link: https://leetcode.com/problems/minimum-window-substring/description/?envType=study-plan-v2&envId=top-interview-150

Given two strings s and t of length m and n respectively, return the minimum window sibstring of s such that every character in t including duplicates is included in the window.

If there is no such substring, return the empty string "".



Sliding window approach
- asssign 2 pointers L, R
- R: expands the current window
- L: contracts a given window

"""


from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        m = len(s)
        n = len(t)

        dict_t = Counter(t) # Counter({'A': 1, 'B': 1, 'C': 1})

        required = len(dict_t)

        l, r = 0, 0 # start by pointing the 1st element of the string

        formed = 0 # to keep track of how many unique char in t are present in the current window

        window_counts = {}  # dictionary which keeps a count of all the unique char in the current window

        ans = float("inf"), None, None # (window_length, left, right)

        while r < len(s):
            # Add one char from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            
            while l <= r and formed == required:
                character = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]









sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"

print(sol.minWindow_sliding_window(s, t))