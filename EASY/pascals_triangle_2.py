"""
Problem Link: https://leetcode.com/problems/pascals-triangle-ii/description/

1. BruteForceRecursion
- Utilize the property of Pascal's triangle.
Say we have a function getNum(rowIndex, colIndex) which gives us the colIndex number in the rowIndex row.
We could simply build the kth row by repeatedly calling getNum for columns 0 to k.

Time Complexity: O(2^k)
Space Complexity: O(k) + O(k) ~= O(k)

2. Dynamic Programming
Store the repetting results of intermediate recursive calls. (use memoization)
"""


class Solution:
    def getRow_BruteForceRecursion(self, rowIndex):
        def getNum(row, col):
            if row == col or row == 0 or col == 0:
                return 1
            return getNum(row - 1, col - 1) + getNum(row - 1, col)

        ans = []
        for i in range(rowIndex + 1):
            ans.append(getNum(rowIndex, i))
        return ans
    
    def getRow_DP(self, rowIndex):
        cache = {}

        def getNum(row, col):
            if (row, col) in cache:
                return cache[(row, col)]
            
            if row == col or row == 0 or col == 0:
                cache[(row, col)] = 1
                return 1
            
            cache[(row, col)] = getNum(row - 1, col - 1) + getNum(row - 1, col)
            return cache[(row, col)]
        
        ans = []
        for i in range(rowIndex + 1):
            ans.append(getNum(rowIndex, i))
        return ans


sol = Solution()
rowIndex = 3
print(sol.getRow_DP(rowIndex))