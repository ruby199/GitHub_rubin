"""
Problem Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].


"""

from typing import Counter


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i] and j != i:
                    count += 1
            result.append(count)
        return result



sol = Solution()
nums = [8,1,2,2,3]
print(sol.smallerNumbersThanCurrent(nums))