"""
Problem Link: https://leetcode.com/problems/sort-colors/description/?envType=daily-question&envId=2024-06-12

"""

class Solution:
    def sortColors(self, nums) -> None:
        if len(nums) < 2:
            return nums
        
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1


sol = Solution()
nums = [2,0,2,1,1,0]
sol.sortColors(nums)
print(nums) # Expected Output: [0,0,1,1,2,2]