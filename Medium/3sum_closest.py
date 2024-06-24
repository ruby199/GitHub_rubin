"""
Problem Link: https://leetcode.com/problems/3sum-closest/description/

"""

class Solution:
    def threeSumClosest(self, nums, target):
        # Time Limit Exceeded

        size = len(nums)

        if size == 3:
            return sum(nums)

        nums.sort()

        current_sum = float('inf')

        for i in range(0, size - 2):
            for j in range(i + 1, size - 1):
                for k in range(j + 1, size):
                    newSum = nums[i] + nums[j] + nums[k]
                    if abs(newSum - target) < abs(current_sum - target):
                        current_sum = newSum
        
        return current_sum


    def threeSumClosest_twoPointers(self, nums, target):
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                current_sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - current_sum) < abs(diff):
                    diff = target - current_sum
                if current_sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
                
        return target - diff



# Test Cases 

sol = Solution()

nums = [-1,2,1,-4]
target = 1
print(sol.threeSumClosest_twoPointers(nums, target)) # Expected output: 2 (-1 + 2 + 1 = 2)
        
nums = [0,0,0]
target = 1
print(sol.threeSumClosest_twoPointers(nums, target)) # Expected output: 0 (0 + 0 + 0 = 0)