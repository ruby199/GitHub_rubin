"""
Problem Link: https://leetcode.com/problems/add-binary/description/

Sol1: 
- Time & Space Complexity: O(n)
- This solution manually compares each digit of the two strings, taking into account all possible cases (both 1, both 0, one 1 and one 0) and the carry from the previous addition.

Sol2: 
- Time & Space Complexity: O(n)
- This solution reverses the strings and adds corresponding digits, handling the carry. 
- More readable.

"""

class Solution:
    # Runtime: Beats 56.32% of users with Python3
    # Memory: Beats 58.82% of users with Python3
    def addBinary(self, a, b):
        res = []
        carry = 0

        diff = abs(len(a) - len(b))

        if len(a) > len(b):
            b = "0" * diff + b
        elif len(a) < len(b):
            a = "0" * diff + a

        for i in range(len(a) - 1, -1, -1):
            if a[i] == "1" and b[i] == "1":
                if carry == 1:
                    res.append("1")
                else:
                    res.append("0")
                    carry = 1

            elif (a[i] == "1" and b[i] == "0") or (a[i] == "0" and b[i] == "1"):
                if carry == 1:
                    res.append("0")
                else:
                    res.append("1")
            elif a[i] == "0" and b[i] == "0":
                if carry == 1:
                    res.append("1")
                    carry = 0
                else:
                    res.append("0")

        if carry != 0:
                res.append("1")
        
        return "".join(res[::-1])

    # Runtime: Beats 51.89% of users with Python3
    # Momory: Beats 57.30% of users with Python3
    def addBinary2(self, a, b):
        a, b = a[::-1], b[::-1] # Reverse both strings
        carry = 0
        result = []

        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0

            total = digitA + digitB + carry
            carry = total // 2

            result.append(str(total % 2))

        if carry:
            result.append("1")

        return ''.join(result[::-1])


sol = Solution()

print(sol.addBinary("1010", "1011"))