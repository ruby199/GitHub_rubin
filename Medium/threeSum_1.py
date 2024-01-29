"""
[TwoSum]
problem link: https://leetcode.com/problems/two-sum/description/

[ThreeSum]
problem link: 
"""

def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        else:
            seen[nums[i]] = i



print(twoSum([2, 4, 9, 6, 5], 10))


def threeSum(nums):
    # sorts the array and use two pointer approach
    nums.sort()
    answer = []

    for i in range(len(nums) - 2): # since we need at least 3 numbers to sum up
        if nums[i] >0:
            break # since we know that i is the smallest among l, r, i
        if i > 0 and nums[i] == nums[i - 1]: # to avoid duplicates
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r: # inner loop (using 2 pointers)
            total = nums[i] + nums[l] + nums[r] # calculate the total i, l, r
            # three possiblities
            if total < 0:   # bc we need to make the total larger
                l += 1
            elif total > 0:
                r -= 1
            else:
                # if we found a solution, add it to our answer list
                triplet = [nums[i], nums[l], nums[r]]
                answer.append(triplet)
                
                # check 2 extra things:
                while l < r and nums[l] == triplet[1]:
                    l += 1
                while l < r and nums[r] == triplet[2]:
                    r -= 1
    return answer



    


