"""
Problem Link: https://leetcode.com/problems/reverse-string-ii/

"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        count = len(s)

        l = 0
        # while l + k - 1 < count: <- This cannot handle the remaining part of the string
        while l < count:
            end = min(l + k, count) # Key change! to handle the remaining parts of the string
            substring = s[l: end]
            substring = substring[::-1]
            # substring = s[l: end][::-1]
            s = s[:l] + substring + s[end:]
            l += 2 * k
        return s

    def reverseStr_list(self, s: str, k: int) -> str:
        s = list(s)  # Convert to list for easier manipulation
        for start in range(0, len(s), 2 * k):
            # Reverse the first k characters in the current 2k block
            s[start:start + k] = reversed(s[start:start + k])
        return ''.join(s)  # Convert list back to string and return



# s = "abcdefg"
# k = 2
    
sol = Solution().reverseStr("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39)

print(sol)
print(sol == "fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqllgsqddebemjanqcqnfkjmi") # check the failing test case


sol2 = Solution().reverseStr("abcdefg", 8)
print(sol2 == "gfedcba") # check the failing test case
