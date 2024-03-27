        rows, cols = len(grid), len(grid[0])
        # Memoization dictionary to store the state of each (row, col, diff) and if it leads to a valid path
        memo = {}

        def dfs(row, col, diff):
            # If out of bounds, return False
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            # If at the destination, check if diff is 0 (equal number of 0's and 1's)
            if row == rows - 1 and col == cols - 1:
                return diff == 0
            # If this state has been visited, return its stored value
            if (row, col, diff) in memo:
                return memo[(row, col, diff)]

            # Calculate the new diff based on the current cell's value
            new_diff = diff + (1 if grid[row][col] == 1 else -1)

            # Explore the next cells to the right and down
            validPath = dfs(row + 1, col, new_diff) or dfs(row, col + 1, new_diff)
            
            # Store the result in memo and return it
            memo[(row, col, diff)] = validPath
            return validPath

        # Start from the top-left corner with an initial diff of 0
        return dfs(0, 0, 0)