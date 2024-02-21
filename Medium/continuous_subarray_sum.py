"""
Problem Link: https://leetcode.com/problems/continuous-subarray-sum/description/

[DEF] Prefix Sum Algorithm:
- A prefix sum array is another array prefixSum[] of the same size, such that the value of prefixSum[i] is arr[0] + arr[1] + arr[2] . . . arr[i].

[DEF] Pigeonhole Principle: if you have more pigeons than pigeonholes, at least one pigeonhole must contain at least two pigeons
- In this probelm, if more prefix sums than possible remainders -> at least 2 prefix sum must share the same remainder 


Time Complexity: O(n) 
Space Complexity: O(n) // Hash Table

"""
class Solution:
    def checkSubarraySum(self, nums, k):
        remainder = {0: -1} # hash map remainder -> end index (handles edge case: we don't want to immediately return true if the first value has remainder of 0)
        total = 0

        # iterate through nums using enumerate (index, value)
        for i, n in enumerate(nums):
            total += n
            r = total % k # k: input parameter
            
            if r not in remainder:
                remainder[r] = i

            elif i - remainder[r] > 1: # curr index and remainder[r] index(we've seen the remainder) have length greater than 1 (distance of index i and r should be at least 2)
                return True # we found the solution
        
        return False


sol = Solution()

nums = [23,2,4,6,7]
k = 6
print(sol.checkSubarraySum_1(nums, k))