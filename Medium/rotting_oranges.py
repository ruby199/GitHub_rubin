from collections import deque

class Solution:
    def orangesRotting(self, grid):
        q = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if (row < 0 or row >= ROWS or
                        col < 0 or col >= COLS or
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
                    if fresh == 0:
                        break
            time += 1

        return time if fresh == 0 else -1

# def get_grid_input():
#     ROWS = int(input("Enter the number of rows: "))
#     grid = []
#     for i in range(ROWS):
#         row = list(map(int, input(f"Enter row {i + 1} (space-separated 0, 1, or 2): ").split()))
#         grid.append(row)
#     return grid

def main():
    solution = Solution()
    test_cases = [
        [[2,1,1],[1,1,0],[0,1,1]],  # Test case 1
        [[2,1,1],[0,1,1],[1,0,1]],  # Test case 2
        [[0,2]],                    # Test case 3
        # Add more test cases as needed
    ]

    for i, grid in enumerate(test_cases, 1):
        result = solution.orangesRotting(grid)
        print(f"Test Case {i}: {grid}")
        print(f"Minutes until all non-isolated oranges rot: {result}\n")

if __name__ == "__main__":
    main()