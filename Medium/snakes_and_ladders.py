"""
Problem Link: https://leetcode.com/problems/snakes-and-ladders/description/

Objective: To find the least number of moves required to reach the final square of a given board. 

[DEF] Breadth-First Search (BFS): Algorithm used for traversing or searching tree and graph data structures.
It starts at a selected node and explores all of its neighbors at the current depth level before moving to the nodes at the next level. BFS typically uses a queue to keep track of the nodes to be explored and is known for its ability to find the shortest path in an unweighted graph.

BFS is particularly useful in scenarios where you need to find the shortest path or need to explore all options evenly before deciding on a path.

Why BFS? -> Because it explores all possible moves from each square in a level-by-level manner when we are trying to find the shortest path.

"""


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board) # since n x n

        board.reverse() # reverse the board to start from the bottom left

        def intToPos(square):
            # Convert a square number to its corresponding row and column
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2: # if odd row number
                c = length - 1 - c # reverse the column for Boustrophedon style
            return [r, c]
        
        q = deque() # for BFS
        q.append([1, 0]) # [square, moves]
        visit = set()
        while q:
            square, moves = q.popleft()

            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                if board[r][c] != -1: # If there is a snake or ladder
                    nextSquare = board[r][c] # move to the snake/ladder destination
                if nextSquare == length * length: # if the final square is reached
                    return moves + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1 # return -1 if the final square cannot be reached