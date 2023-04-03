# Given an integer array nums sorted in non-decreasing order(=increasing order but having same values), return an array of the squares of seach number sorted in non-decreasing order

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        res = []
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] * nums [l] > nums[r] * nums[r]:
                res.append(nums[l] * nums[l])
                l += 1

            else:
                res.append(nums[r] * nums[r])
                r -= 1
        
        return res[::-1] # reverse