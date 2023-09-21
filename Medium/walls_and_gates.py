from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0]) # Set the number of rows and columns
        visit = set() # Keep track of the visited cells using a set
        q = deque() # Initialize a queue to perform BFS (Breadth-First Search)

        # A utility function to add neighboring rooms to the queue
        def addRoom(r, c):
            # Check if the coordinates are out of boundary, already visited, or a wall (indicated by -1)
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit or rooms[r][c] == -1):
                return 
            # Mark this cell as visited and add to the queue
            visit.add((r, c))
            q.append([r, c])

        # Initialize the queue with gates (indicated by - in the rooms matrix)
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        dist = 0
        while q: # Perform BFS to update each room's distance to its nearest gate
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist # Set the distance of the current room

                # Add the neighboring rooms to the queue for further processing
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1 # Increment the distance for the next level