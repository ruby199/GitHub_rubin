"""
Problem Link: https://leetcode.com/problems/number-of-closed-islands/description/?envType=study-plan-v2&envId=google-spring-23-high-frequency

Problem Description:
    Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

    Return the number of closed islands.

Topics: array, DFS, BRS, union find, matrix



* Edge cases: - any island touching the grid's border cannot be a closed island. 

Step:
1. eliminate border-connected land -> iterate over the grid's border
2. count and mark the closed islands. (DFS/BFS from that cell)
"""
class Solution:
    def closedIsland(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0 # keep track of the number of closed islands
        # visited = {} # keep track of visited cells
        
        def dfs(x, y):
            # edge cases: if current cell is on the border - it cannot be part of a closed island
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return False
            
            if grid[x][y] == 1 or grid[x][y] == -1:
                return True
            
            grid[x][y] = -1 # instead of using a visited dict, mark as visited directly on the board
            isClosed = True
            
            # visited[(x, y)] = True
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            for dx, dy in directions:# explore all directions
                nx, ny = x + dx, y + dy
                isClosed = dfs(nx, ny) and isClosed

            return isClosed

        # iterate over all cells of gird for every cells
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        count += 1
        
        return count

# grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    

grid = [
    [0,0,1,1,0,1,0,0,1,0],
    [1,1,0,1,1,0,1,1,1,0],
    [1,0,1,1,1,0,0,1,1,0],
    [0,1,1,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,1,1,1,0],
    [0,1,0,1,0,1,0,1,1,1],
    [1,0,1,0,1,1,0,0,0,1],
    [1,1,1,1,1,1,0,0,0,0],
    [1,1,1,0,0,1,0,1,0,1],
    [1,1,1,0,1,1,0,1,1,0]
]

sol = Solution()
print(sol.closedIsland(grid))