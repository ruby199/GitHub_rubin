class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return  0 # if needle is empty, first matching is index 0
        
        # Use longest prefix suffix (use lps array)
        # prefix: every substring strarting at the beginning
        lps = [0] * len(needle)
 
        prevLPS, i = 0, 1 # use two pointers
        while i < len(needle): # to fill lps array
            if needle[i] == needle[prevLPS]:
                lps[i] = preLPS + 1
                prevLPS += 1 # since characters are equal in this case
                i += 1
            elif prevLPS == 0:
                    lps[i] = 0
                    i += 1
            else:
                prevLPS = lps[prevLPS - 1]

        i = 0 # ptr for haystack
        j = 0 # ptr for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1

                else:
                    j = lps[j - 1]
            if j == len(needle): # if we found the match
                return i - len(needle)
            
        return -1



        # for i in range(len(haystack) + 1 - len(needle)):
        #     if haystack[i: i + len(needle)] == needle:
        #         return i

            # for j in range(len(needle)):
            #     if haystack[i+j] != needle[j]:
            #         break
            #     if j == len(needle) - 1:
            #         return i

        # return -1

"""
The Knuth-Morris-Pratt (KMP) algorithm is a string searching algorithm that finds the occurrence of a pattern string within a larger string. It is an efficient algorithm that has a time complexity of O(n+m) where n and m are the lengths of the strings. The KMP algorithm uses a pre-processing technique to create a partial match table for the pattern string, which is called the longest prefix suffix (LPS) table. The LPS table contains the length of the longest proper prefix of the pattern that matches the proper suffix of the same pattern. This table is created before searching the pattern in the main string. Once the LPS table is created, the KMP algorithm compares the pattern string with the main string from left to right. When a mismatch occurs, the algorithm uses the LPS table to skip over the characters that have already been matched. This avoids the unnecessary comparisons and makes the algorithm more efficient. The KMP algorithm can be implemented using two pointers. The first pointer iterates through the main string, and the second pointer iterates through the pattern string. When a match is found, both pointers are incremented. When a mismatch occurs, the second pointer is moved back to the position specified by the LPS table and compared with the character in the main string at the current position of the first pointer. The KMP algorithm is used in various applications, including text editors, compilers, and bioinformatics. It is especially useful when the pattern string is long, and the main string is large, as it avoids unnecessary comparisons and improves the efficiency of the algorithm.
"""