"""
Problem Link: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/?envType=study-plan-v2&envId=google-spring-23-high-frequency

Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.

Topics: Array, Two Pointers, Stack, Greedy, Sorting, Monotonic Stack
"""


class Solution:
    def findUnsortedSubarray_stack(self, nums) -> int:
        stack = []
        l, r = len(nums), 0
        
        # Finding the left boundary using stack
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)
        
        stack.clear()

        # Finding the right boundary using the stack
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)
        
        return 0 if r - l < 1 else r - l + 1

    def findUnsortedSubarray_withoutExtraSpace(self, nums) -> int:
        """
        Makes two passes through the array to determine the boundaries by comparing the elements with their extreme values seen so far.
        """
        n = len(nums)
        max_seen, min_seen = float('-inf'), float('inf')
        start, end = -1, -1

        # Find the right boundary
        for i in range(n):
            if nums[i] < max_seen:
                end = i
            max_seen = max(max_seen, nums[i])
        
        # Find the left boundary
        for i in range(n - 1, -1, -1):
            if nums[i] > min_seen:
                start = i

            min_seen = min(min_seen, nums[i])

        return 0 if end - start < 1 else end - start + 1


sol = Solution()
nums = [2,6,4,8,10,9,15]
print(sol.findUnsortedSubarray_stack(nums)) # Expected Output: 5
print(sol.findUnsortedSubarray_withoutExtraSpace(nums)) # Expected Output: 5