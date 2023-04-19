class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) # 0 is not a good default
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1 # reset
                continue

            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n) # python can compare 3 by max function
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res
