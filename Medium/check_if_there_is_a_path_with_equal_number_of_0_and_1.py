"""
Problem Link: https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/description/?envType=study-plan-v2&envId=google-spring-23-high-frequency

Problem Description: 
- You are given a 0-indexed m x n binary matrix grid. You can move from a cell (row, col) to any of the cells (row + 1, col) or (row, col + 1). 
- Return true if there is a path from (0, 0) to (m - 1, n - 1) that visits an equal number of 0's and 1's. Otherwise return false.

-> meaning, you can move right/down only 

Topics: array, dynamic programming, matrix

"""

class Solution:
    def isThereAPath_1(self, grid) -> bool: 
        # This solution does not work! (Time Limit Exceeded error occured)
        # -> as a solution: use DP

        rows, cols = len(grid), len(grid[0])

        def dfs(row, col, zeros, ones):
            # Base condition: if out of bounds
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == -1:
                return False

            # Count zeros and ones
            if grid[row][col] == 0:
                zeros += 1
            else:  # This means grid[row][col] == 1
                ones += 1

            # Check if current cell is bottom-right and has equal zeros and ones
            if row == rows - 1 and col == cols - 1:
                return zeros == ones

            # Mark the cell as visited
            temp = grid[row][col]
            grid[row][col] = -1

            # Explore the next cells to the right and down
            result = dfs(row + 1, col, zeros, ones) or dfs(row, col + 1, zeros, ones)

            # Unmark the cell after exploring (to keep the grid unchanged)
            grid[row][col] = temp
            return result

        return dfs(0, 0, 0, 0)  # Start from top-left corner
    


    def isThereAPath_dp(self, grid) -> bool:
        rows, cols = len(grid), len(grid[0])

        if (rows * cols) % 2 != 0:
            return False  # If odd number of cells, it's impossible to have equal ones and zeros

        memo = {}

        def dfs(row, col, zeros, ones):
            if row == rows - 1 and col == cols - 1:
                return zeros == ones and zeros + ones == rows + cols - 1
            
            if (row, col, zeros, ones) in memo:
                return memo[(row, col, zeros, ones)]
            
            memo[(row, col, zeros, ones)] = False  # Default to False unless a path proves otherwise

            if col + 1 < cols:  # Move right
                if grid[row][col + 1] == 0:
                    if dfs(row, col + 1, zeros + 1, ones):
                        memo[(row, col, zeros, ones)] = True
                        return True
                else:
                    if dfs(row, col + 1, zeros, ones + 1):
                        memo[(row, col, zeros, ones)] = True
                        return True

            if row + 1 < rows:  # Move down
                if grid[row + 1][col] == 0:
                    if dfs(row + 1, col, zeros + 1, ones):
                        memo[(row, col, zeros, ones)] = True
                        return True
                else:
                    if dfs(row + 1, col, zeros, ones + 1):
                        memo[(row, col, zeros, ones)] = True
                        return True

            return False
        
        initial_zeros = 1 if grid[0][0] == 0 else 0
        initial_ones = 1 - initial_zeros
        
        return dfs(0, 0, initial_zeros, initial_ones)

grid = [[0,1,0,0],[0,1,0,0],[1,0,1,0]] # Expected: True
sol = Solution()
print(sol.isThereAPath_1(grid))
print(sol.isThereAPath_dp(grid))