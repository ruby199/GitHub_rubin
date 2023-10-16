class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # sort the input array and then use the sliding window of size k
        nums.sort()
        l, r = 0, k - 1

        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l, r = 1 + 1, r + 1
        return res