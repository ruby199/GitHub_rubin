"""
Problem Link: https://leetcode.com/problems/set-mismatch/?envType=daily-question&envId=2024-01-22
"""

# Runtime: Beats 64.40% of users with Python3
# Memory: Beats 86.03% of users with Python3
class Solution:
    def findErrorNums(self, nums):
        nums.sort()  # O(n log n)
        duplicate = None
        missing = None

        ### Fixed
        if nums[0] != 1:
            missing = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                duplicate = nums[i]
            elif nums[i] > nums[i - 1] + 1:
                missing = nums[i - 1] + 1

        if nums[-1] != len(nums):
            missing = len(nums)

        return [duplicate, missing]

# Runtime: Beats 66.21% of users with Python3
# Memory: Beats 86.03% of users with Python3
def findErrorNums2(nums):
    duplicate = -1
    missing = 1

    for num in nums:
        # Check if the number at index |num| - 1 (to account for 0-indexing) has been seen before
        if nums[abs(num) - 1] < 0:
            duplicate = abs(num)
        else:
            # Mark the number at this index as seen by making it negative
            nums[abs(num) - 1] *= -1

    # Identify the missing number
    for i in range(1, len(nums)):
        if nums[i] > 0:
            missing = i + 1  
            break

    return [duplicate, missing]

        
sol = Solution()
nums = [1, 2, 3, 4, 5, 5]
print(sol.findErrorNums(nums))