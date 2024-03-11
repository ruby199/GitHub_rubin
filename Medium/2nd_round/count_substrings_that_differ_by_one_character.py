"""
Problem Link: https://leetcode.com/problems/count-substrings-that-differ-by-one-character/description/
Topics: Hash Table, String, Dynamic Programming


We could see that there's likely n^2 solution for this problem.
Time Complexity : O(mn)
Space Complexity : O(mn)

"""

class Solution:
    def countSubstrings_dp(self, s: str, t: str) -> int:
        dpl = [[0 for y in range(len(t))] for x in range(len(s))]
        dpr = [[0 for y in range(len(t))] for x in range(len(s))]

        # Initialze dpl, dpr
        for i in range(len(s)):
            for j in range(len(t)):
                if i != 0 and j != 0:
                    dpl[i][j] = dpl[i-1][j-1] + 1 if s[i-1] == t[j-1] else 0
        
        for i in range(len(s)-1, -1, -1):
            for j in range(len(t)-1, -1, -1):
                if i != len(s) - 1 and j != len(t) - 1:
                    dpr[i][j] = dpr[i+1][j+1] + 1 if s[i+1] == t[j+1] else 0
        cnt = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] != t[j]:
                    lop = dpl[i][j] + 1
                    rop = dpr[i][j] + 1
                    cnt += lop * rop 
                
        return cnt
                    

    def countSubstrings_brute_force(self, s: str, t: str) -> int:
        def countMatches(s, t):
            count = 0
            
            # Iterate over each starting index in s
            for i in range(len(s)):
                # over each starting index in t
                for j in range(len(t)):
                    mismatch = 0
                    k = 0
                    # expand the substring as long as we have at most one mismatch
                    while i + k < len(s) and j + k < len(t) and mismatch <= 1:
                        if s[i + k] != t[j + k]:
                            mismatch += 1
                        
                        # Only ocunt if there's exactly one mismatch
                        if mismatch == 1:
                            count += 1
                        k += 1
            return count
        
        return countMatches(s, t)







# Test example cases
sol = Solution()

s1 = "ab"
t1 = "bb"

s2 = "aba"
s3 = "baba"

print(sol.countSubstrings(s1, t1))