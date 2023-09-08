# Define the Solution class
from ast import List
import math


class Solution:
    # Define the minEatingSpeed method that determines the minimum speed Koko can eat bananas to finish within 'h' hours
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Initialize 'l' to 1 and 'r' to the maximum value in piles. These will be the boundaries for our binary search.
        l, r = 1, max(piles)
        # Initialize 'res' to 'r'. It will store the minimum speed required for Koko.
        res = r
        
        # Continue searching while 'l' is less than or equal to 'r'
        while l <= r:
            # Calculate the mid-point of 'l' and 'r' which will be our current speed 'k' for testing
            k = (l + r) // 2
            # Initialize 'hours' to 0. It will store the number of hours needed to eat all bananas at speed 'k'
            hours = 0
            # Iterate through each pile in 'piles'
            for p in piles:
                # For each pile, calculate the hours required at speed 'k' and accumulate the result in 'hours'
                hours += math.ceil(p / k)
            
            # Check if Koko can eat all bananas within 'h' hours at speed 'k'
            if hours <= h:
                # If so, update the result with the current speed (or keep the smaller speed if previously found one)
                res = min(res, k)
                # Adjust the upper boundary 'r' for the binary search to find a possibly smaller 'k'
                r = k - 1
            else:
                # If Koko cannot eat all bananas in 'h' hours at speed 'k', adjust the lower boundary 'l' to find a larger 'k'
                l = k + 1
        # Return the final result, which is the minimum speed at which Koko can eat all bananas within 'h' hours
        return res
