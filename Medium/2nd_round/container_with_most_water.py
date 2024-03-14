"""
Problem Link: https://leetcode.com/problems/container-with-most-water/description/

Topics: Array, Two Pointers, Greedy

"""
class Solution:
    def maxArea(self, height) -> int:
        if len(height) < 2:
            return 0
        
        maxArea = 0
        l, r = 0, len(height) - 1

        while l < r:
            curArea = (r - l) * min(height[l], height[r])
            maxArea = max(maxArea, curArea)

            # we need to move the shorter side
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
            


        


sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))