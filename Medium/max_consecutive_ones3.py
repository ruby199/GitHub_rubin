"""
Problem Link: https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75

Description:
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

In any sliding window based problem we have two pointers. One right pointer whose job is to expand the current window and then we have the left pointer whose job is to contract a given window. At any point in time only one of these pointers move and the other one remains fixed.

Even though it doesn't track the maximum length explicitly throughout, the algorithm always maintains the largest possible window under the constraints given by adjusting both pointers optimally. Once the loop finishes, the pointers define the maximum window because:
    1. The right pointer has tried to include as many elements as possible.
    3. The left pointer has contracted the window just enough to adhere to the constraint of flipping at most k zeros.

"""

class Solution:
    def longestOnes(self, nums, k):
        left = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]

            if k < 0:
                k += 1 - nums[left]
                left += 1
        
        return right - left + 1




sol = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(sol.longestOnes(nums, k)) # Expected output: 6