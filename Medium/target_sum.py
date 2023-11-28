class Solution:
    def findTargetSumWays_dp(self, nums, target):
        # Using Top-Down Dynamic programming
        memo = {}  # Hash map to store number of ways to achieve a certain sum at a certain index.
                   # Key: (index, current_sum) : num_of_ways

        def dp(index, cur_sum):
            # Base case: if the end of the array is reached, check if the current sum equals the target.
            if index == len(nums):
                return 1 if cur_sum == target else 0  # Return 1 if there is a way, 0 otherwise

            # Check if the current state is already computed and stored in memo
            if (index, cur_sum) in memo:
                return memo[(index, cur_sum)]

            # Recursively explore adding and subtracting the current number
            add = dp(index + 1, cur_sum + nums[index])
            subtract = dp(index + 1, cur_sum - nums[index])

            # Store the computed result in the memo dictionary
            memo[(index, cur_sum)] = add + subtract

            # Return the computed result
            return memo[(index, cur_sum)]

        # Start the recursion from index 0 and initial sum of 0
        return dp(0, 0)

    def findTargetSumWays_dfs(self, nums, target):
        def dfs(index, current_sum):
            # Base case: if all elements are used, check if the current sum equals the target
            if index == len(nums):
                return 1 if current_sum == target else 0

            # Recursive calls for adding and subtracting the current number
            add = dfs(index + 1, current_sum + nums[index])
            subtract = dfs(index + 1, current_sum - nums[index])

            # Total ways for the current index
            return add + subtract

        # Start the DFS from the first element with an initial sum of 0
        return dfs(0, 0)



def test_findTargetSumWays():
    solution = Solution()

    # Test case 1
    nums = [1, 1, 1, 1, 1]
    target = 3
    expected = 5
    assert solution.findTargetSumWays_dp(nums, target) == expected, f"DP Test 1 Failed: Expected {expected}, got {solution.findTargetSumWays_dp(nums, target)}"
    assert solution.findTargetSumWays_dfs(nums, target) == expected, f"DFS Test 1 Failed: Expected {expected}, got {solution.findTargetSumWays_dfs(nums, target)}"

    # Test case 2
    nums = [1]
    target = 1
    expected = 1
    assert solution.findTargetSumWays_dp(nums, target) == expected, f"DP Test 2 Failed: Expected {expected}, got {solution.findTargetSumWays_dp(nums, target)}"
    assert solution.findTargetSumWays_dfs(nums, target) == expected, f"DFS Test 2 Failed: Expected {expected}, got {solution.findTargetSumWays_dfs(nums, target)}"

    # Add more test cases as needed
    # ...

    print("All tests passed!")

# Run the test function
test_findTargetSumWays()