"""
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = { 0 : 1 } # hash map - 1 way we can add up to zero

        for total in range(1, target + 1): # 1 to target value
            dp[total] = 0 # initialize to 0 (0 ways)
            for n in nums: # look at subproblem
                dp[total] += dp.get(total - n, 0) #dp of total, get total - n if exist but if not simply return zero. 
        
        return dp[target]
