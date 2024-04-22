"""
Problem Link: https://leetcode.com/problems/count-strictly-increasing-subarrays/description/
Topics: Array, Math, Dynamic Programming
"""

class Solution:
    # Runtime: Beats 80.39% of users with Python3
    # Memory: Beats 66.67% of users with Python3
    def countSubarrays_greedy(self, nums):
        count = 0
        i = 0

        while i < len(nums):
            j = i
            while j < len(nums) - 1 and nums[j] < nums[j + 1]:
                j += 1
            
            # Length of the increasing segment
            length = j - i + 1

            # Add the count of all subarrays that can be formed in this segment
            count += (length * (length + 1)) // 2 

            i = j + 1

        return count

    def countSubarrays_dynamic_programming(self, nums):
        # Runtime: Beats 27.45% of users with Python3
        # Memory : Beats 9.80% of users with Python3
        if not nums:
            return nums
        
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        total = dp[0]

        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1 # reset the count at this index to 1 (the increasing sequence is broken)
            total += dp[i]
        return total


sol = Solution()

nums = [1,3,5,4,4,6]
print(sol.countSubarrays_greedy(nums)) # 10 expected

sol = Solution()

nums2 = [1,2,3,4,5]
print(sol.countSubarrays_dynamic_programming(nums2)) # 15 expected
