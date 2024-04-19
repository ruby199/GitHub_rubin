"""
Problem Link: https://leetcode.com/problems/number-of-islands/description/?envType=daily-question&envId=2024-04-19

Topics: Array, DFS, BFS, Union Find, Matix

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

BFS:
 

"""

import collections

class Solution:
    def numIslands(self, grid) -> int:
        if not grid: # empty grid with no island
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set() # marking where we visitied (could also use 2D grid)
        islands = 0

        # iterative bfs
        def bfs(r, c):
            # que is used for bfs usually
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q: # while que is not empty, expend our island
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        # visit every single elements
        for r in range(rows):
            for c in range(cols):
                # if visited.
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands


        




sol = Solution()


grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

print(sol.numIslands(grid)) # expected output: 1


