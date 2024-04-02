"""
Problem Link: https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150


sol 1. built-in split & reverse
    - Time Complexity: O(M), Memory Complexity: O(N)

sol 2. trim the white spaces, reverse the whole string, and then reverse each word. (Note: python = immutable strings )
    - Time Complexity: O(M), Memory Complexity: O(N)

sol 3. 2 passes approch with a deque. (move along the string, word by word, push each new word in front of the deque. convert the deque back into a string)
    - Time Complexity: O(M), Memory Complexity: O(N)

"""

from collections import deque


class Solution:
    def reverseWords_sol1(self, s: str) -> str:
        # print(s.split()) # ['the', 'sky', 'is', 'blue']
        return " ".join(reversed(s.split()))

    def reverseWords_sol2(self, s: str) -> str:
        def reverse(l, left, right):
            while left < right:
                l[left], l[right] = l[right], l[left]
                left, right = left + 1, right - 1
        
        def trim_spaces(s):
            left, right = 0, len(s) - 1
            
            # remove the leading space
            while left <= right and s[left] == ' ':
                left += 1
            while left <= right and s[right] == ' ':
                right -= 1
            
            # reduce multiple spaces to single one
            output = []
            while left <= right:
                if s[left] != ' ':
                    output.append(s[left])
                elif output[-1] != ' ':
                    output.append(s[left])
                left += 1
            # print(output) # ['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e']
            return output

        def reverse_each_word(l):
            n = len(l)
            start = end = 0

            while start < n:
                # go to the end of the word
                while end < n and l[end] != ' ':
                    end += 1
                reverse(l, start, end - 1)
                start = end + 1
                end += 1
            
        l = trim_spaces(s)
        reverse(l, 0, len(l) - 1)

        reverse_each_word(l)

        return ''.join(l)
            

    def reverseWords_sol3(self, s: str) -> str: # deque of words
        left, right = 0, len(s) - 1

        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1
        
        while left <= right and s[right] == ' ':
            right -= 1

        # after this, left will be the index of the 1st non-space char from the start of the string 
        # right will be the index of the last non-space character from the end of the string
    
        d, word = deque(), []
        
        # push word by word in front od deque
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))
        # print(d) # deque(['blue', 'is', 'sky', 'the'])

        return ' '.join(d)

        



# Testing 

sol = Solution()
s = "the sky is blue"
print(sol.reverseWords_sol1(s))

print(sol.reverseWords_sol2(s))

print(sol.reverseWords_sol3(s))
