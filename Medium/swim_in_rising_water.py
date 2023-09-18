class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid) # get the size of the grid (n x n)
        visit = set() # A set to keep track of visited nodes.
        # Initialize the min-heap (priority queue) with the starting point (0, 0) and its elevation.
        minH = [[grid[0][0], 0, 0]]  # (time/max-height, r, c)

        # A list of possible directions for moving in the grid
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0)) # Mark the starting point (0,0) as visited.

        # Dijkstra's main loop. Continue as long as there are nodes in the priority queue.  
        while minH:
            # Pop the node with the minimum time/max-height
            t, r, c = heapq.heappop(minH)

            # If we've reached the destination, return the required time. 
            if r == N - 1 and c == N -1: # reached the destination
                return t
            
            # Explore the neighbors of the current node. 
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc # Calculate the position of the neightboring cell. 

                # Check if the neighboring cell is valid (within grid bounds and not visited)
                if (neiR < 0 or neiC < 0 or
                    neiR == N or neiC == N or
                    (neiR, neiC) in visit):
                    continue
                # Mark the neighboring cell as visited. 
                visit.add((neiR, neiC))

                # Push the neighboring cell into the priority queue. 
                # The priority (time/max-height) is the maximum of the current time and the cell's elevation. 
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])



