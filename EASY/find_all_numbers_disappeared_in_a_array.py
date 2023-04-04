class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # mark existing
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i]) # if number appeared, change to negative (-1 is just for marking it if exit)

        res = []
        for i, n in enumerate(nums):
            if n > 0: # numbers that did not appeared
                res.append(i + 1) # as it's index

        return res