"""
Problem Link: https://leetcode.com/problems/4sum/description/

Approach 4Sum:
- Generalize solution for kSum problems.
- Base Case: when k==2, it switches to a two-pointer approach to find the pair solution. 


Approach 4Sum_1:
    1. Sort the array
    2. Iterate with Two Pointers
    3. Avoid duplicates
    4. 2Sum approach for the last two elements


Time Complexity: O(n^3)
Space Complexity: O(m + n), where m is the number of quadruplets found
"""


class Solution:
    def fourSum(self, nums, target):
        res = []
        quad = []
        nums.sort()

        def kSum(k, start, target): # k: how many remaining values are we allowed to use
            if k != 2:
                for i in range(start, len(nums) - k + 1): # until the last 3 values
                    if i > start and nums[i] == nums[i - 1]: # skip duplicates
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i]) # Reduce k and narrow down the target
                    quad.pop() # Backtrack to explore other combinations
                return

            # base case, two sum II solved with 2 pointers
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]]) # add the found combination
                    l += 1
                    while l < r and nums[l] == nums[l - 1]: # skip duplicates
                        l += 1
        
        kSum(4, 0, target) # start the recursion with k = 4
        return res


    def fourSum_1(self, nums, target):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            # Avoid duplicates for the 1st number
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                # Avoid duplicates for the 2nd number
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        # Skip the duplicates for the 3rd number
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip the duplicates for the 4th number
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return result


nums = [1,0,-1,0,-2,2]
target = 0


sol = Solution()

print(sol.fourSum_1(nums, target))
