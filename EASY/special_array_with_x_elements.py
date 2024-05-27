"""
Special Array With X Elements Greater Than or Equal X

Problem Link: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/?envType=daily-question&envId=2024-05-27


Description:

You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.
Notice that x does not have to be an element in nums.
Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

"""


class Solution:
    def specialArray(self, nums):
        # Beats 98.90% of users with Python3
        # Beats 62.87% of users with Python3
        def check_special(x):
            count = 0
            for num in nums:
                if num >= x:
                    count += 1
            return count == x
        
        for x in range(len(nums) + 1):
            if check_special(x):
                return x
        return -1
    

sol = Solution()
nums = [3,5]
print(sol.specialArray(nums))   # Expected output: 2 (There are 2 values (3 and 5) that are greater than or equal to 2.)