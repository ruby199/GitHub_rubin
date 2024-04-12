"""
Problem Link: https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150

Topics: String, Stack
"""

import re


class Solution:
    def simplifyPath(self, path):
        # Beats 98.97% of users with Python3
        parts = [part for part in path.split('/') if part and part != '.'] # all "/"s are converted to empty ''
        stack = []
        
        for part in parts:
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return '/' + '/'.join(stack)









path = "/home//foo/"
sol = Solution().simplifyPath(path)
print(sol)