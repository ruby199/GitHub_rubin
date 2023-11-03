class Solution:
    def gridGame(self, grid: List[List[int]]):
        # Find the number of columns in the grid
        N = len(grid[0])

        # copy the first and second row of the grid for manipulation
        # preRow1 will be used for the prefix sums of the top row.
        # preRow2 will be used for the prefix sums of the bottom row. 
        preRow1, preRow2 = grid[0].copy(), grid[1].copy()

        # Calculate the prefix sums for both rows.
        for i in range(1, N):
            preRow1[i] += preRow1[i - 1] # Add the previous value to the current, accumulating sums for top row
            preRow2[i] += preRow2[i - 1] # Do the same for the bottom row
        
        res = float("inf") # initialize result with infinity, which will hold the minimum points the second robot can get

        # Iterate through each possible column where the first robot might drop to the bottom row
        for i in range(N):
            top = preRow1[-1] - preRow1[i]  # the remaining points on the top row before the first robot's move at column i
            bottom = preRow2[i - 1] if i > 0 else 0 # if i is 0, then no points are accumulated in the bottom row
            # The second robot will choose the path with more points after the first robot
            secondRobot = max(top, bottom)

            # Update the result with the min of the current result and points collected by the second robot. 
            res = min(res, secondRobot)
        
        return res
