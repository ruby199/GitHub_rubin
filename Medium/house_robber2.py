class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time complexity: O(n)
        # Memery complexity: O(1)
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1])) # skip index 0 & skip the last index




    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob # rob2 will contain the max amount of the array

        return rob2
