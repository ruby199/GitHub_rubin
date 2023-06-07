class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use Hash Set for detecting duplicates (unique hash set for every single rows/cols)
        cols = collections.defaultdict(set) # set is all particular values in that col
        rows = collections.defaultdict(set) # set is all particular values in that row
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # if empty -> skip
                    continue
                if (board[r][c] in rows[r] or # already occured in the current row
                    board[r][c] in cols[c] or # already occured in the current col
                    board[r][c] in squares[(r // 3, c // 3)]): # already occured in the current square
                    return False # have duplicates -> not valid
                # If valid: update the board
                cols[c].add(board[r][c]) 
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        return True
