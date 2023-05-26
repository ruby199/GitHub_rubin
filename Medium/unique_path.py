class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n # the bottom row. 

        for i in range(m - 1): # go through all of the other row except for the last one
            newRow = [1] * n
            for j in  range(n - 2, -1, -1): # avoid out of bound
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
