"""
Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150


"""

class Solution:    
    def removeDuplicates(self, nums):
        l = 1

        for r in range(1, len(nums)):

            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l


sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums))
