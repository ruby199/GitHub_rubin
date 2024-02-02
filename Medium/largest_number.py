"""
Problem Link: https://leetcode.com/problems/largest-number/description/

Sol1. Apply the Key Function (lambda x: x*3)
- The key function is applied to each element in the list to create a new list (not actually created though) where each number is repeated 3 times  (e.g., '9' becomes '999')
- This solution does not handle all of the test cases (Note: constraints " 0 <= nums[i] <= 109")

    Time complexity: O(n log n)
    Space complexity: O(n)

Sol2. Use Bubble sort based on the concatenation of the pairs of numbers in string format 
- For example, when comparing 9 and 34, we are comparing 923 and 349. 

    Time complexity: O(n^2) because of the bubble sort
    Space complexity: O(n)

Sol2. Define a custom comparison function compare that dictates the sorting order based on the concatenation of pairs of numbers in string format. - This is the most practical solution.

    Time complexity: O(n log n)
    Space complexity: O(n) 

"""

from functools import cmp_to_key


class Solution:
    def largestNumber_1(self, nums) -> str:
        # fails testcase: nums = [999999991,9]

        nums_str = [str(item) for item in nums] 
        # sort_str_nums = sorted(nums_str, key=lambda x: (x[0], max(x), x), reverse=True)

        nums_str.sort(key=lambda x: x*3, reverse=True)

        return ''.join(nums_str)
    
    def largestNumber_2(self, nums) -> str:
        nums_str = [str(item) for item in nums]
        n = len(nums_str)

        for i in range(n):
            for j in range(0, n - i - 1):
                comp1 = nums_str[j] + nums_str[j + 1]
                comp2 = nums_str[j + 1] + nums_str[j]
                if comp1 < comp2:  # If the current pair is in the wrong order
                    nums_str[j], nums_str[j + 1] = nums_str[j + 1], nums_str[j]  # Swap

        result = ''.join(nums_str)
        if result[0] == '0':  # Handle the edge case where the largest number is '0'
            return '0'
        return result


    def largestNumber_3(self, nums) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)
        
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        
        nums = sorted(nums, key=cmp_to_key(compare))

        # handle [0, 0] instead of "00", we would like to return "0"

        return str(int("".join(nums)))




sol = Solution()
result = sol.largestNumber_3([3, 30, 34, 5, 9])
print(result)