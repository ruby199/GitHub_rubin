"""
Problem Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.
"""

class Solution:
    def findDuplicates1(self, nums):
        seen = set()
        result = []
        for num in nums:
            if num in seen:
                result.append(num)
        
            seen.add(num)

        return result

    def findDuplicates2(self, nums): # Cycle Sort
        def swap(nums, index1, index2):
            temp = nums[index1]
            nums[index1] = nums[index2]
            nums[index2] = temp

        n = len(nums)
        i = 0
        while i < n:
            correctIdx = nums[i] - 1
            if nums[i] != nums[correctIdx]:
                swap(nums, i, correctIdx)
            else:
                i += 1
        
        # Any elements not at the index that corresponds to their value are duplicates
        result = []

        for i in range(n):
            if nums[i] != i + 1:
                result.append(nums[i])
        return result





sol = Solution()
nums = [4,3,2,7,8,2,3,1]
print(sol.findDuplicates1(nums))
print(sol.findDuplicates2(nums))
