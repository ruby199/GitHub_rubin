"""
Problem Link: https://leetcode.com/problems/different-ways-to-add-parentheses/description/

Different Ways to Add Parentheses

Topics: Math, String, Dynamic Programming, Recursion, Memoization 


1) Recursion


"""


class Solution:
    def diffWaysToCompute(self, expression: str):

        def isOperator(ch):
           return ch in {'+', '-', '*'}


        def getDiffWays(i, j, expression): # returns number of ways of expression[i...j] 
            res = []
            if j < i:
                return res
            
            if all(not isOperator(char) for char in expression[i:j+1]):
                res.append(int(expression[i:j+1]))
                return res

            # if j - i + 1 <= 2: # length of substring is 1 or 2
            #     res.append(int(expression[i:j + 1]))
            #     return

            for ind in range(i, j + 1):
                if isOperator(expression[ind]):
                    op = expression[ind]
                    # if char at ind is operator
                    left = getDiffWays(i, ind - 1, expression)
                    right = getDiffWays(ind + 1, j, expression)

                    # try all options for left & right operand
                    for l in left:
                        for r in right:
                            if op == '+':
                                res.append(l + r)
                            elif op == '-':
                                res.append(l - r)
                            elif op == '*':
                                res.append(l * r)

            return res
        
        n = len(expression)
        return getDiffWays(0, n - 1, expression)





sol = Solution()
expression = "2*3-4*5"
print(sol.diffWaysToCompute(expression)) # Expected Output: [-34,-14,-10,-10,10]

"""

Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

2 * 3 - 4 * 5

"""