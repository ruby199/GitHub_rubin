class Solution:
    def searchInsert(self, nums, target) -> int:

        # binary search
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            
        return l


sol = Solution()
nums = [1,3,5,6]
target = 2
print(sol.searchInsert(nums, target))