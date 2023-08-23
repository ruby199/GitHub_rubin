class Solution:
    def missingNumber(self, nums: List[int]) -> int: # binary prob.
        # using XOR operation. Sum[all vals from range] - Sum[all vals from nums]
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        return res