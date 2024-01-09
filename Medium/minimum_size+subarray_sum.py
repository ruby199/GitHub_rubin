"""
Problem Link: https://leetcode.com/problems/minimum-size-subarray-sum/

Goal of the problem:
- To find the minimal length of a contiguous subarray of which the sum is greater than or equal to a target value.

Sliding Window Technique: 
- Used to perform required operations on a subset of elements of an array or a list.
- This subset (or window) is often a range of consecutive elements, and you can either move the window to the right or change its size.
- This technique is especially useful for problems that ask for things like maximum sums, lengths, or other similar aggregations of subarrays.

"""


class Solution:
    # Does not pass test case with target = 213, nums = [12,28,83,4,25,26,25,2,25,25,25,12]
    # Output = 7, Expected = 8
    # Sorting alters the original order of the elements, which is crucial for finding the minimal length subarray in its original sequence. 
    def minSubArrayLen_trial_1(self, target, nums):
        nums.sort()
        sum_nums = sum(nums)

        if sum_nums < target:
            return 0
        if sum_nums == target:
            return len(nums)
        
        result = 0
        cur_sum = 0
        for cur in range(len(nums) - 1, -1, -1):
            cur_sum += nums[cur]
            result += 1
            if cur_sum >= target:
                break
        
        return result
    
    # Using sliding windows technique
    # Runtime: Beats 98.84%of users with Python3
    # Memory: Beats 24.34%of users with Python3
    def minSubArrayLen_trial_2(self, target, nums):
        left, right = 0, 0
        total = nums[left]
        cur_result = float('inf')

        while right < len(nums):
            if total >= target:
                cur_result = min(cur_result, abs(left - right) + 1)
                total -= nums[left]
                left += 1
            else:
                right += 1
                if right < len(nums):
                    total += nums[right]
        
        return 0 if cur_result == float('inf') else cur_result

            

# solution = Solution()
# target = 213
# nums = [12,28,83,4,25,26,25,2,25,25,25,12]

# print(solution.minSubArrayLen_trial_2(target, nums)) # Output = 7, Expected = 8


def test_minSubArrayLen():
    solution = Solution()

    # Test cases
    test_cases = [
        {"target": 7, "nums": [2,3,1,2,4,3], "expected": 2},
        {"target": 4, "nums": [1,4,4], "expected": 1},
        {"target": 11, "nums": [1,1,1,1,1,1,1,1], "expected": 0},
        # Add more test cases here
    ]

    for i, test_case in enumerate(test_cases):
        target = test_case["target"]
        nums = test_case["nums"]
        expected = test_case["expected"]
        result = solution.minSubArrayLen_trial_2(target, nums)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run the test
test_minSubArrayLen()
