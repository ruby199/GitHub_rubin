"""
Search a 2D MAtrix

You are given mxn matrix with the following two properties:
1. Each row is sorted in increasing order. 
2. The first integer of each row is greater than the last integer of the previous row. 

given int target, return true if target is in matric or false otherwise. 

Write a solution in O(long(m*n)) time complexity.
"""

# Using the prop 1. each element is sorted. 
# Using Binary Search. O(log n)
# every single value: m long n

# Using the prop 2. 
# Using Binary Search and finding which row to search for first. 
# first binary search: O(log n) search, then the second one: O(log m + log n)



from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the number of rows and columns in the matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bot = 0, ROWS - 1

        # Perform binary search on rows to narrow down the potential row
        while top <= bot:
            row = (top + bot) // 2
            
            if target > matrix[row][-1]:
                top = row + 1  # Target might be in the rows below the middle row
            elif target < matrix[row][0]:
                bot = row - 1  # Target might be in the rows above the middle row
            else:
                break  # Target is within the range of the middle row, exit the loop
        
        # Check if the top pointer exceeds the bottom pointer, indicating no potential row
        if not (top <= bot):
            return False
        
        # Calculate the final row where the target might be located
        row = (top + bot) // 2
        
        l, r = 0, COLS - 1
        
        # Perform binary search on columns to find the target within the chosen row
        while l <= r:
            m = (l + r) // 2
            
            if target > matrix[row][m]:
                l = m + 1  # Target might be in the columns to the right of the middle column
            elif target < matrix[row][m]:
                r = m - 1  # Target might be in the columns to the left of the middle column
            else:
                return True  # Target found, exit the function and return True
        
        return False  