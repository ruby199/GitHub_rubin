"""
Problem Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=study-plan-v2&envId=leetcode-75
Topics: Hash Table, String, Backtracking

"""

class Solution:
    # def letterCombinations(self, digits: str):
        # digitToChar = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        # res = []

        # def backtrack(i, curString):
        #     if len(curString) == len(digits):
        #         res.append(curString)
        #         return
            
        #     for char in digitToChar[digits[i]]:
        #         backtrack(i + 1, curString + char)
            
        # if digits:
        #     backtrack(0, "")
        
        # return res

    def letterCombinations(self, digits: str):
        if not digits:
            return []
        
        digitToChar = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        combinations = []

        def backtrack(index, path):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return

            possible_letters = digitToChar[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
            
        backtrack(0, [])
        return combinations
        
        
    

sol = Solution()
digits = "23"

print(sol.letterCombinations(digits))