"""
Problem Link: https://leetcode.com/problems/permutations-ii/description/

Description: Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]


Problem Approach: Backtracking
- Backtracking is a general algorithm for finding all (or some) solutions to some problems with constraints.
It incrementally builds candidates to the solutions, and abandons a candidate as soon as it determines that the candidate cannot possibly lead to a solution.


"""

from typing import Counter


class Solution:
    def permuteUnique(self, nums):
        result = []

        def backtrack(comb, counter):
            if len(comb) == len(nums):
                result.append(list(comb))
                return
            
            for num in list(counter):
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb, counter)
                    comb.pop()
                    counter[num] += 1
    
        # print(Counter(nums)) # Counter({1: 2, 2: 1})
        
        backtrack([], Counter(nums))

        return result


sol = Solution()
nums = [1,1,2]
print(sol.permuteUnique(nums))
        