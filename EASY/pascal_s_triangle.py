"""
Problem Link: https://leetcode.com/problems/pascals-triangle/description/

[1] generate1 Function (Recursive Approach)
Problem: This function experiences a Time Limit Exceeded (TLE) issue when executing the test case with numRows=25. 
This is due to its recursive nature.
- Time Complexity: Higher than O(n^2) due to repeated calculations in recursive calls.
- Space Complexity: Higher due to recursive call stack and repeated construction of rows.

[2] generate2 Function (Dynamic Programming Approach)
Performance: It significantly outperforms generate1 with a runtime that beats 97.96% of Python3 submissions and a memory usage that beats 17.52%.
- Time Complexity: O(n^2), as each element of the triangle is computed exactly once.
- Space Complexity: O(n^2), for storing the entire triangle.

"""

class Solution:
    # generate1 -> Time Limit Exceeded (TLE) issue wuth testcase numRows=25
    def generate1(self, numRows):
        def pascal(remainingRows):
            if remainingRows == 0:
                return []
            if remainingRows == 1:
                return [[1]]
            
            # Generate previous Row
            prev_row = pascal(remainingRows - 1)[-1]
            row = [1]
            for i in range(1, len(prev_row)):
                row.append(prev_row[i - 1] + prev_row[i])
            row.append(1)
            return pascal(remainingRows - 1) + [row]

        return pascal(numRows)

    # Runtime: Beats 97.96% of users with Python3
    # Memory: Beats 17.52% of users with Python3
    def generate2(self, numRows):
        if numRows == 0:
            return []

        # Initialize the triangle with the first row
        triangle = [[1]]

        for i in range(1, numRows):
            row = [1]  # Start each row with 1
            # Construct the row
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)  # End each row with 1

            triangle.append(row)

        return triangle



sol = Solution()
print(sol.generate(5))