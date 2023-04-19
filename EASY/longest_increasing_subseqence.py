class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # Brute Force - DFS
        # go through every possible subsequence.
        # 2^n subsequence

        # DFS with Cache (Dynamic programming) better than brute force(DFS) O(n^2)
            # LIS[3] = 1
            # LIS[2] = max(1, 1+LIS[3])
            # LIS[1] = max(1, 1+LIS[2]. 1+LIS[3])
            # LIS[0] = max(1, 1+LIS[1], 1+LIS[2]. 1+LIS[3])
        LIS = [1] * len(nums)

        for i in range(len(1)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+ LIS[j])
        
        return max(LIS)
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Brute Force - DFS
        # go through every possible subsequence.
        # 2^n subsequence
        
        # Dynamic Programming Approach - O(n^2)
        # DFS with Cache (Dynamic programming) better than brute force(DFS) O(n^2)
            # LIS[3] = 1
            # LIS[2] = max(1, 1+LIS[3])
            # LIS[1] = max(1, 1+LIS[2]. 1+LIS[3])
            # LIS[0] = max(1, 1+LIS[1], 1+LIS[2]. 1+LIS[3])
        
        # Create a list of length n, initialized to 1
        LIS = [1] * len(nums)
        
        # Loop through each element in the list
        for i in range(len(nums)):
            # Loop through all previous elements
            for j in range(i):
                # If a previous element is less than the current element,
                # update the length of the LIS for the current element
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        # Return the maximum length of LIS
        return max(LIS)
