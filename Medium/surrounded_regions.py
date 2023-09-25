class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Return immediately if the board is empty
        if not board:
            return
        
        # Get the dimensions of the board
        m, n = len(board), len(board[0])

        # Helper function for DFS to mark the 'O's that should not be flipped
        def dfs(i, j):
            # Base case: Check for out-of-bounds of if the current cell is bot 'O'
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            
            board[i][j] = 'T'
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(i + x, j + y)
        
         # Mark 'O's on the top and bottom border
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
    
        # Mark 'O's on the left and right border
        for i in range(1, m-1):
            dfs(i, 0)
            dfs(i, n - 1)
        
        # Traverse the board to flip the 'O's and restore the 'T's
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X' 
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
