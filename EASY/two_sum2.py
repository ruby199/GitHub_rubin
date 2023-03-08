# Two Sum II - Input Array Is Sorted

"""
class Solution:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def twoSum(self):
        l ,r = 0, len(self.number)-1
        while l < r:
            curSum = self.number[l] + self.number[r]

            if curSum > self.target:
                r -= 1
            elif curSum < self.target:
                l += 1
            else:
                return str([l + 1, r + 1])

p = Solution([2,7,11,15], 9)
print(p)
"""

from ast import List
from os import name


def twoSum(numbers, target):
    l ,r = 0, len(numbers)-1
    while l < r:
        curSum = numbers[l] + numbers[r]

        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
                    return [l + 1, r + 1]

print(twoSum([2,7,11,15], 9))
