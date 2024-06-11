"""
Problem Link: https://leetcode.com/problems/unique-paths-ii/description/


"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])

        memo = [[-1] * col for _ in range(row)]

        def searchPath(r, c):
            # Check if out of bounds or if there's an obstacle
            if r >= row or c >= col or obstacleGrid[r][c] == 1:
                return 0
            
            # If this cell has been computed, return the stored result
            if memo[r][c] != -1:
                return memo[r][c]
            
            # If at the destination, return 1 path
            if r == row - 1 and c == col - 1:
                return 1
            
            # Recursively count paths from the right and down directions
            right_paths = searchPath(r + 1, c)
            left_paths = searchPath(r, c + 1)

            # store the result in memoization table
            memo[r][c] = right_paths + left_paths

            return memo[r][c]
        
        # Check if start is blocked
        if obstacleGrid[0][0] == 1:
            return 0 

        return searchPath(0, 0)


    def uniquePathsWithObstacles_dp(self, obstacleGrid) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        # starting point
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        # Fill the first row (can only come from the left)
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]

        # Fill the first column 
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]

        # Fill the rest of the dp
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]




sol = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(sol.uniquePathsWithObstacles(obstacleGrid)) # Expected output: 2
print(sol.uniquePathsWithObstacles_dp(obstacleGrid)) # Expected output: 2