"""
Problem Link: https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=leetcode-75

# Binary Search.

Time complexity : O(log_2(n))
Space complexity : O(1)
"""

class Solution:
    def findPeakElement(self, nums):
        # Iterative Binary Search Method
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m + 1] < nums[m]:
                r = m
            else:
                l = m + 1
        
        return l


sol = Solution()
nums = [1,2,1,3,5,6,4] 
print(sol.findPeakElement(nums)) # Expected Output: 1 or 5
        