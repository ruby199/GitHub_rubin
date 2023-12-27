from collections import Counter
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Count the occurrences of each number in nums
        count = Counter(nums)
        # Sort and deduplicate the nums to process them in ascending order
        nums = sorted(list(set(nums)))

        earn1, earn2 = 0, 0 # earn1: the points earned including the prev num, earn2: the points earned including the prev num. 

        # iterate through each unique number in nums
        for i in range(len(nums)):
            curEarn = nums[i] * count[nums[i]] # the current potential earning from the current number
            # can't use both curEarn and earn2
            if i > 0 and nums[i] == nums[i - 1] + 1: # if consecutive, decide whether to take current num or skip
                temp = earn2
                earn2 = max(curEarn + earn1, earn2)
                earn1 = temp
            else:
                # can use both values
                temp = earn2
                earn2 = curEarn + earn2
                earn1 = temp
        
        return earn2
