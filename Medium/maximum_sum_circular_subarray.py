"""
Problem Link: https://leetcode.com/problems/maximum-sum-circular-subarray/?envType=study-plan-v2&envId=top-interview-150

Approach: Calculate the "Minimum Subarray"
"special sum" : the sum of a prefix and a suffix
We can think about it as the sum of all elements, minux a subarray in the middle 


[DEF]"Kadane's algorithm": 
- a dynamic programming technique used to find the max subarray within a given array of numbers.
"""

class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        def kadane_max(nums):
            max_ending_here = max_so_far = nums[0]
            for num in nums[1:]:
                max_ending_here = max(num, max_ending_here + num)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far

        def kadane_min(nums):
            min_ending_here = min_so_far = nums[0]
            for num in nums[1:]:
                min_ending_here = min(num, min_ending_here + num)
                min_so_far = min(min_so_far, min_ending_here)
            return min_so_far
        
        # Calculate the max and min subarray
        maxSum = kadane_max(nums)
        minSum = kadane_min(nums)

        totalSum = sum(nums)

        if minSum == totalSum:
            return maxSum
        
        else:
            return max(maxSum, totalSum - minSum)
        

         

def test_maxSubarraySumCircular():
    solution = Solution()
    
    # Test case 1: Normal case with mixed values
    nums1 = [1, -2, 3, -2]
    assert solution.maxSubarraySumCircular(nums1) == 3, f"Test case 1 failed. Output: {solution.maxSubarraySumCircular(nums1)}"

    # Test case 2: All positive values
    nums2 = [5, -3, 5]
    assert solution.maxSubarraySumCircular(nums2) == 10, f"Test case 2 failed. Output: {solution.maxSubarraySumCircular(nums2)}"

    # Test case 3: All negative values
    nums3 = [-3, -2, -3]
    assert solution.maxSubarraySumCircular(nums3) == -2, f"Test case 3 failed. Output: {solution.maxSubarraySumCircular(nums3)}"

    # Test case 4: Large circular subarray
    nums4 = [3, -1, 2, -1]
    assert solution.maxSubarraySumCircular(nums4) == 4, f"Test case 4 failed. Output: {solution.maxSubarraySumCircular(nums4)}"

    # Test case 5: Edge case with a single element
    nums5 = [1]
    assert solution.maxSubarraySumCircular(nums5) == 1, f"Test case 5 failed. Output: {solution.maxSubarraySumCircular(nums5)}"

    # Test case 6: Large array with positive and negative values
    nums6 = [8, -1, 3, 4]
    assert solution.maxSubarraySumCircular(nums6) == 15, f"Test case 6 failed. Output: {solution.maxSubarraySumCircular(nums6)}"

    # Test case 7: Circular sum is maximum
    nums7 = [5, -3, 5, -3, 5]
    assert solution.maxSubarraySumCircular(nums7) == 12, f"Test case 7 failed. Output: {solution.maxSubarraySumCircular(nums7)}"

    print("All test cases passed!")

# Run the test function
test_maxSubarraySumCircular()