"""
Problem Link: https://leetcode.com/problems/sum-of-subarray-minimums/description/
Topics: Array, Dynamic Programming, Stack, Monotonic Stack

Approach 1: Monotonic Stack - Contribution of Each Element

Question:
"In the given range, find the count of subarrays which contain x"

Approach 2: Monotonic Stack + Dynamic Programming

"""

class Solution:
    def sumSubarrayMins(self, arr) -> int:
        # edge case: if the array is empty
        if not arr:
            return 0
        
        l = len(arr)
        total = 0

        # Brute force (double for loops)
        for start in range(l):
            for end in range(start, l):
                subarray_sum = min(arr[start:end + 1])
                total += subarray_sum
        return total

    def sumSubarrayMins_MonotonicStack(self, arr):
        MOD = 10 ** 9 + 7 # Define the modulo for large numbers
        n = len(arr)
        stack = []
        sumOfMin = 0

        for i in range(n + 1):
            current = arr[i] if i < n else float('-inf')

            while stack and (arr[stack[-1]] > current):
                mid = stack.pop()
                previousSmallerIndex = stack[-1] if stack else -1

                # calculate the contribution of the element that was just poppsed
                left = mid - previousSmallerIndex
                right = i - mid
                contribution = arr[mid] * left * right
                sumOfMin = (sumOfMin + contribution) % MOD
        
            stack.append(i)

        return sumOfMin


sol = Solution()
arr = [3,1,2,4]
print(sol.sumSubarrayMins(arr)) # Exected Output: 17