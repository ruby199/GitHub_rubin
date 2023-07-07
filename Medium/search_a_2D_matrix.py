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




class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bot = 0, ROWS - 1

        while top >= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break 
        
        if not (top <= bot):
            return False
        row = (top +bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target > matrix[row][m]:
                r = m - 1
            else:
                return True

        return False