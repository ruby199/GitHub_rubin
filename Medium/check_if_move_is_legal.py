from typing import List

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        # Get the dimensions of the board.
        ROWS, COLS = len(board), len(board[0])
        
        # Define possible directions: vertical, horizontal, and diagonal.
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1],   # Up, Down, Right, Left
                     [1, 1], [-1, -1], [1, -1], [-1, 1]]  # Diagonals

        # Place the piece on the board.
        board[rMove][cMove] = color

        # Define a helper function to check if placing the piece at the given position 
        # would "capture" any pieces of the opposite color.
        def legal(row, col, colar, direc):
            # Extract the direction.
            dr, dc = direc
            row, col = row + dr, col + dc
            length = 1  # Start with a length of 1 for the current piece.

            # Continue in the direction until you reach the board's edge.
            while (0 <= row < ROWS and 0 <= col < COLS):
                length += 1
                # If there's an empty spot, then no capturing is possible in this direction.
                if board[row][col] == ".": return False
                # If the current piece is of the same color, check if the sequence length 
                # makes capturing possible.
                if board[row][col] == color:
                    return length >= 3
                
                # Move to the next position in the direction.
                row, col = row + dr, col + dc

            # If loop ends without returning, no capture is possible.
            return False

        # Check each direction from the placed piece.
        for d in direction:
            if legal(rMove, cMove, color, d): 
                # If any direction results in a capture, return True.
                return True
        
        # If no directions result in a capture, return False.
        return False
