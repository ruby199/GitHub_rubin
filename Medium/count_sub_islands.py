class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        visit = set()

        def dfs(r, c): # return True if the current island in grid2 is a sub-island of grid1
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                grid2[r][c] == 0 or (r, c) in visit): # out of bounds, is water, or has been visited before
                return True

            visit.add((r, c))
            res = True    
            if grid1[r][c] == 0: # false if current cell is land in grid2 but water in grid1 (not a sub-island)
                res = False
            
            # DFS is then recursively called for the neighboring cells(north, south, east, west) 
            res = dfs(r - 1, c) and res
            res = dfs(r + 1, c) and res
            res = dfs(r, c - 1) and res
            res = dfs(r, c + 1) and res

            return res # if the current island in grid2 is a sub-island of grid1.

        
        count = 0 # number of sub island in grid2
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and (r, c) not in visit and dfs(r, c): # only run dfs on grid2 (not in the same grid/same pos twice)
                    count += 1 # increment result
        
        return count