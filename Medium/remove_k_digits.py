"""
Problem Link: https://leetcode.com/problems/remove-k-digits/description/

Description: Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

For solving this problem - we use Monotonic Stack (increasing order) approach.

Monotonic Stack
- Used when finding the next greater/smaller element in an array is required.
- Monotonic: entirely non-increasing/non-decreasing

# Time Complexity: O(n)
# Memory Complexity: O(n)

"""

class Solution:
    def removeKdigits_1(self, num: str, k: int) -> str:
        # Runtime Error:
        # Due to limitation of the int function in python, this solution does not pass test cases with extremely long strings of digits

        stack = []
        # iterate every char in nums
        for char in num:
            while k > 0 and stack and stack[-1] > char: # check if the stack is non-empty & current char is smaller than the last digit in the stack
                k -= 1
                stack.pop() # since the current char is smaller

            stack.append(char)

        # concatenate the remaining elements from the stack
        stack = stack[:len(stack) - k]
        res = "".join(stack) 

        return str(int(res)) if res else "0"


    def removeKdigits_fixed(self, num: str, k: int) -> str:
        stack = []

        for char in num:
            while k > 0 and stack and stack[-1] > char:
                k -= 1
                stack.pop()
            stack.append(char)
        
        stack = stack[:len(stack) - k]
        res = "".join(stack)
        
        # Manually remove leading zeros.
        index = 0
        while index < len(res) - 1 and res[index] == '0':
            index += 1
        res = res[index:]

        # If the resulting string is empty, return "0"
        return res if res else "0"


    def removeKdigits(self, num: str, k: int) -> str:
        st = list()
        for n in num:
            while st and k and st[-1] > n:
                st.pop()
                k -= 1
            
            if st or n != '0': # prevent leading zeros
                st.append(n)
                
        if k: # not fully spent
            st = st[0:-k]
            
        return ''.join(st) or '0'

sol = Solution().removeKdigits("10200", 1)
print(sol)