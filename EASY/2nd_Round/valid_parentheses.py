"""
Problem Link: https://leetcode.com/problems/valid-parentheses/description/

"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {")" : "(", "]" : "[", "}": "{"}
    
        for char in s:
            if char in parentheses:
                if stack and stack[-1] == parentheses[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False
                




sol = Solution()
s = "()[]{}"
print(sol.isValid(s)) # Expected output: true