"""
Problem Link: https://leetcode.com/problems/word-search/description/

Backtracking(Brute Force Sol): 
- Algorithm that tries to find a solution incrementally by trying different options and undoing them if they lead to a dead end.
- Used when searching for a path in a maze or solving puzzles. When a dead end is reached, the algortihm backtracks to the previous decision point & explores a different path until a solution is found.

Depth-First Search(DFS)

Reference:
 
https://www.geeksforgeeks.org/introduction-to-backtracking-data-structure-and-algorithm-tutorials/

"""

class Solution:
    def exist(self, board, word):
        ROWS, COLS = len(board), len(board[0])

        # Depth-first search
        def dfs(r, c, i, path=set()): # Pass in values: [1] r, c: board position [2] i: current char [3] path set
            # Base case: if the current index matches the length of the word, word is found
            if i == len(word):
                return True

            # Check the invalid cases
            if (r < 0 or c <0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path):
                print("r, c, path:", r, c, path)
                return False

            # Add the current cell to the path
            path.add((r,c))

            print("cur path: ", path)
            print("i:", i)
            print("letter: ", word[i])

            # Recursively explore all adjacent directions
            res = (dfs(r + 1, c, i + 1, path) or 
                   dfs(r - 1, c, i + 1, path) or 
                   dfs(r, c + 1, i + 1, path) or 
                   dfs(r, c - 1, i + 1, path))
            
            # Backtrack: remove the cell from the path
            path.remove((r, c))
            
            # Return the result of DFS
            return res
        
        # Iterate over every cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                # Start DFS from this cell if the first character matches
                if dfs(r, c, 0): return True


        # If the word cannot be found, return False
        return False

sol = Solution()


board = 	[["A","B","C","E"],
["S","F","C","S"],
["A","D","E","E"]]


word = "SEE"

sol.exist(board, word)