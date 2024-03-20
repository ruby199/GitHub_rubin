"""
Problem Link: https://leetcode.com/problems/minimum-falling-path-sum/description/

Topics: Array, Dynamic Programming, Matrix

"""

class Solution:
    def minFallingPathSum(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])

        for r in range(1, rows): # start from the second row
            for c in range(cols):
                if c == 0:
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c+1])
                elif c == cols - 1:
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c-1])
                else:
                    matrix[r][c] += min(matrix[r-1][c-1], matrix[r-1][c], matrix[r-1][c+1])

        return min(matrix[-1])

sol = Solution()
# matrix = [[-19,57],[-40,-5]]
matrix = [[2,1,3],[6,5,4],[7,8,9]]
print(sol.minFallingPathSum(matrix))