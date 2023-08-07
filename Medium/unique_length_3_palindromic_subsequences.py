class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set() # a set that will store tuples representing palindromic subsequences in the form of (middle, outer) - Since there are 26 characters in the English alphabet (assuming lowercase letters)
        left = set() #  left side of the current character while traversing the string s
        right = collections.Counter(s) # counter object created using collections.Counter, which will store the counts of each character in the string s

        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])

            for j in range(26):
                c = chr(ord('a') + j)
                if c in left and c in right:
                    res.add((c, s[i], c))
            
            left.add(s[i])

        return len(res)
