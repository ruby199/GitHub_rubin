"""
Problem Link: https://leetcode.com/problems/repeated-dna-sequences/description/

Topics: Hash Table, String, Bit Manipulation, Sliding Window, Rolling Hash, Hash function

Hash Set approach: O(n)
[DEF] Hash Set: Hash Set derives from AbstractSet and implements the Set interface. Only unique elements are stored in HashSet.

Use mapping of:
    A -> 00
    C -> 01
    G -> 10
    T -> 11

Memory Opt:
    We could use bit manipulation and have a integer of 32 bits.
    instead of using a string of 10 characters where each character is 8 bits long.
    (80bits->20bits)

"""


class Solution:
    def findRepeatedDnaSequences(self, s: str):
        seen, res = set(), set()

        for l in range(0, len(s) - 9):
            cur = s[l:l+10]
            if cur in seen:
                res.add(cur)
            else:
                seen.add(cur)
        return list(res)



sol = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(sol.findRepeatedDnaSequences(s)) # Output: ["AAAAACCCCC","CCCCCAAAAA"]
