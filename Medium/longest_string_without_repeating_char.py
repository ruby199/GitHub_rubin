class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # technique - sliding window
        charSet = set()

        l = 0 # left pointer
        res = 0

        # right pointer would change
        for r in range(len(s)):
            while s[r] in charSet:
                # update window if already in the set
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        
        return res
