"""
Height Checker

Problem Link: https://leetcode.com/problems/height-checker/description/?envType=daily-question&envId=2024-06-10

"""

class Solution:
    def heightChecker(self, heights) -> int:
        prev = heights.copy()
        heights.sort()
        # print(heights)
        count = 0 
        for i in range(len(heights)):
            if heights[i] != prev[i]:
                count += 1
        return count


    def heightChecker_bubblesort(self, heights):
        def bubble_sort():
            n = len(sorted_heights)

            for i in range(n - 1):
                for j in range(n - i - 1):
                    if sorted_heights[j] > sorted_heights[j + 1]:
                        sorted_heights[j], sorted_heights[j + 1] = (
                            sorted_heights[j + 1],
                            sorted_heights[j],
                        )
        sorted_heights = heights[:]
        bubble_sort()

        count = 0
        for i in range(len(sorted_heights)):
            if heights[i] != sorted_heights[i]:
                count += 1
        return count
    



sol = Solution()
heights = [1,1,4,2,1,3]
print(sol.heightChecker(heights)) # Expected output: 3

heights = [1,2,3,4,5]
print(sol.heightChecker_bubblesort(heights)) # Expected output: 0

