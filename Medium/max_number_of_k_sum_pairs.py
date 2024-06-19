"""
Problem Link: https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

You are given an integer array, nums and an integer k.
In one operation, you can pick 2 numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

"""

from collections import defaultdict


class Solution:
    def maxOperations_bruteForce(self, nums, k) -> int:
        count_map = defaultdict(int)
        count = 0

        # build the hashmap with count of occurence of every element in array
        for num in nums:
            count_map[num] += 1
        
        for num in nums:
            current = num
            complement = k - num
            if count_map[current] > 0 and count_map[complement] > 0:
                if current == complement and count_map[current] < 2:
                    continue
                count_map[current] -= 1
                count_map[complement] -= 1
                count += 1
        return count

    def usingHashMap_singlePass(self, nums, k) -> int:
        """
        Solution that iterates over the array only once.
        """
        count_map = defaultdict(int)
        count = 0

        for num in nums:
            complement = k - num
            if count_map[complement] > 0:
                # remove complement from the map
                count_map[complement] -= 1
                count += 1
            else:
                count_map[num] += 1

        return count

        



sol = Solution()

nums = [3,1,3,4,3]
k = 6

print(sol.maxOperations_bruteForce(nums, k)) # Expected output: 1
print(sol.usingHashMap_singlePass(nums, k))