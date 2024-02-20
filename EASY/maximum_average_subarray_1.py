"""
Probelm Link: https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

Approach: Sliding Window Technique. (which is useful for fixed-size subarray problems)
- By reusing the computations from the previous window, the need for redundant calculations are significantly reduced. 

Time Complexity: O(n), where n is the length of the array
Space Complexity: O(1), since we are using a constant amount of space regardless of the input size.
"""


class Solution:
    def findMaxAverage(self, nums, k) -> float:
        # Sliding window algorithm
        largest = sum(nums[:k])
        cur_sum = largest
        
        for i in range(1, len(nums) - k + 1):
            cur_sum = cur_sum - nums[i-1] + nums[i+k-1]
            # print(cur_sum)
            largest = max(cur_sum, largest)
        return largest / k



sol = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print(sol.findMaxAverage(nums, k))