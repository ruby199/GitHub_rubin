"""
Problem Link: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/

Topics: String, Backtracking



Time Complexity:  O(3 * 2^n), where n is the recursion depth (=string length)
- Note: total number of calls resembles a binary tree's growt and 3 * because initial character can be chosen from 3 options

Memory Complexity: O(n * k)
- n: depth of the recursion call stack
- 3 * 2^(n-1) for all possible happy strings but since we could stop at the 'k'th string we only have to go as fas as k 

"""

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # n: length of the happy strings
        # kth string

        letters = ['a', 'b', 'c']
        happy_strings = []


        def happystring(cur_str):
            if len(cur_str) == n:
                happy_strings.append(cur_str)
                return
            
            for letter in letters:
                if not cur_str or cur_str[-1] != letter:
                    happystring(cur_str + letter)

        
        happystring("")

        return happy_strings[k-1] if len(happy_strings) >= k else ""


sol = Solution()
n = 1
k = 3
print(sol.getHappyString(n, k))