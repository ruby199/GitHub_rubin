"""
Problem Link: https://leetcode.com/problems/product-of-array-except-self/description/

[DEF] Prefix Sum: the each value in the new array is the sum of the prev sum and the current value (diagonally added)
Prefix sum algorithm is mainly used for range query and the complexity of prefix sum algorithm is O(n).


Correct Approach for this problem: 
- Left: 
- Right: 
- Time Complexity(as the problem required): O(n)

"""

from math import prod


class Solution:
    def productExceptSelf_wrong(self, nums):
        # Time Limit Exceeded for extremely long test cases
        length = len(nums)
        result = [1] * length
        for i in range(length):
            temp = [num for num in nums] # repeated work
            del temp[i] 
            result[i] = prod([num for num in temp])
             
        return result
    
    def productExceptSelf_fixed(self, nums):
        # Still having the sample problem: Time Limit Exceeded for extremely long test cases
        length = len(nums)
        result = [1] * length
        for i in range(length):
            # print(i)
            # print(nums[:i])
            # print(nums[i+1:])
            result[i] = prod(nums[:i] + nums[i+1:]) # avoided the repeated work, though did not pass the test case
        return result

    def productExceptSelf_prefix_sum_alg(self, nums):
        """
        Runtime Complexity: O(n) + O(n) + O(n) = O(n)
        Memory Complexity: O(n)
        """
        # Runtime: Beats 14.43% of users with Python3
        # Memory: Beats 30.23% of users with Python3
        length = len(nums)
        left = [1] * length
        right = [1] * length
        # nums = [2,3,4,5,6]

        for i in range(1, length):
            left[i] = nums[i - 1] * left[i - 1]
        # print(left) # [1, 2, 6, 24, 120]
            
        for i in range(length - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]
        # print(right) # [360, 120, 30, 6, 1]
        
        output = [ left[i] * right[i] for i in range(length)]
        # print(output) # [360, 240, 180, 144, 120]
        
        return output

# [Note] Constraints: the algorithm must run in O(n) time and without using the division operation
    def productExceptSelf_optimized(self, nums):
        # Runtime: Beats 60.11% of users with Python3
        # Memory: Beats 69.32% of users with Python3
        length = len(nums)
        product = [1] * length

        for i in range(1, length):
            product[i] = product[i-1] * nums[i-1]

        right = nums[-1]
        for i in range(length - 2, -1, -1):
            product[i] *= right
            right *= nums[i]

        return product



sol = Solution()
# print(sol.productExceptSelf_prefix_sum_alg([1,2,3,4]))
print(sol.productExceptSelf_prefix_sum_alg([2,3,4,5,6]))
