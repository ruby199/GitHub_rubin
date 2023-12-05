class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        ROWS, COLS = len(grid), len(grid[0])

        # Set to keep track of visited cells
        visit = set()

        # Define the DFS function
        def dfs(r, c):
            # Check for out-of-bounds, water, or already visited cell
            if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r, c) in visit):
                return 0

            # Mark the current cell as visited
            visit.add((r, c))

            # Calculate the area of this island, and explore adjacent cells
            # 1 is for the current cell, and the rest are from adjacent cells
            return (1 + dfs(r + 1, c)+ dfs(r - 1, c)+ dfs(r, c + 1)+ dfs(r, c - 1))

        
        # Initialize max area
        area = 0
        # Iterate through each cell in the grid
        for r in ROWS:
            for c in COLS:
                # Update the max area with the maximum between current max and the area returned by dfs
                area = max(area, dfs(r, c))
        # Return the maximum area found
        return area
