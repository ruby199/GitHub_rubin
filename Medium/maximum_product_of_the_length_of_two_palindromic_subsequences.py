class Solution:
    def maxProduct(self, s: str) -> int:
        N, pali = len(s), {} # pali is a dictionary that will store info about palindromic subsequences found in the input string. bitmask : length

        # Generate all possible subsequences and store palindromes
        for mask in range(1, 2 ** N):
            subseq = ""
            for i in range(N):
                if mask & ( 1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]: # if it is palindromic(it reads the same forwards and backwards)
                pali[mask] = len(subseq) # it is stored in the dictionary along with its length
            
        # Calculate the Maximum Product of Lengths of Two Non-Intersecting Palindromic Subsequences
        res = 0
        for m1 in pali:
            for m2 in pali:
                if m1 & m2 == 0:
                    res = max(res, pali[m1] * pali[m2])
        
        return res
