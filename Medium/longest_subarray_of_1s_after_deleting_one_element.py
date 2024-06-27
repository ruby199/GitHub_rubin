"""
Problem Link: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.


"""


class Solution:
    def longestSubarray(self, nums):
        left = 0 # start of the window
        zeros = 0 # keeps count of how many zeros are in the current window
        max_len = 0 # (right-left) after deleting one element

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
                
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left)

        return max_len


sol = Solution()
nums = [0,1,1,1,0,1,1,0,1]
print(sol.longestSubarray(nums)) # Expected Result: 5