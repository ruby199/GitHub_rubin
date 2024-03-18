"""
Problem Link: https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/


Description: 
- Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Topics: Array, Dynamic Programming, Matrix

if the sum of values == size^2 -> square

e.g. 
[1 1
 1 1] => 4 = size^2 

[1 0
 1 1] => 3 != size^2

 1 1 1
 1 2 2
 1 2 3 

fill each pos as the sum of count of squares ending at each cell (i, j)

"""


class Solution:
    def countSquares(self, matrix) -> int:
        if not matrix:
            return 0
        
        rows = len(matrix)
        columns = len(matrix[0])
        count = 0

        dp = [[0 for _ in range(columns)] for _ in range(rows)]

        for i in range(rows):
            for j in range(columns):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                count += dp[i][j]
        return count

sol = Solution()

matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

print(sol.countSquares(matrix))