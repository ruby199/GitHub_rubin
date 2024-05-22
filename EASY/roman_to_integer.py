"""
Problem Link: https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=google-spring-23-high-frequency


Topics: Hash Table, Math, String

Note:
- The Trick is to use the 'biggest' symbols you can. 
"""



class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return ''
        
        romanToInt = {'I': 1,
                      'V': 5,
                      'X': 10,
                      'L':50,
                      'C': 100,
                      'D': 500,
                      'M':1000}
        
        result = 0
        prevValue = 0

        for char in s:
            currentValue = romanToInt[char]

            if currentValue > prevValue:
                result += currentValue - 2 * prevValue
            else:
                result += currentValue
            
            prevValue = currentValue

        return result
        


sol = Solution()
s = "LVIII"
print(sol.romanToInt(s)) # Expected output: 58
        

