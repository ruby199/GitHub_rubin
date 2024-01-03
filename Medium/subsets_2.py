"""
Backtracking is a recursive, DFS approach. It builds solutions one step at a time and abandons a path as soon as it determines that this path cannot possibly lead to a solution (pruning).

Handling duplicates is crucial. In this problem, sorting the array is helpful since it brings duplicates together (we can skiup ove them during backtracking process)

At each step in backtracking, we have a choice to include/exclude the element (nums[i]). - this binary choice leads to the construction of all possible combination.

"""


class Solution:
    def subsetsWithDup(self, nums):
        res = []  # Initialize an empty list to store the result.
        nums.sort()  # Sort the numbers to bring duplicates together.

        def backtrack(i, subset): 
            # i is the current index in nums, subset is the current subset being constructed.
            if i == len(nums): 
                # Base case: if i equals the length of nums, meaning we've considered every element.
                # The current subset is then copied and added to the result list.
                res.append(subset.copy())
                return
            
            # Include nums[i] in the subset.
            subset.append(nums[i])
            backtrack(i + 1, subset)  # Recursive call to consider further elements.
            subset.pop()  # Remove nums[i] from the subset after exploring subsets including nums[i].
            
            # Skipping over duplicates.
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1  # Increment i to skip duplicates.
            backtrack(i + 1, subset)  # Recursive call to explore subsets that exclude nums[i] and its duplicates.
        
        backtrack(0, [])  # Start the backtracking process from the first element.
        return res  # Return the list of all unique subsets.

# Example test
sol = Solution()
test_nums = [1, 2, 2]
print("Testing subsetsWithDup with nums:", test_nums)
print("Result:", sol.subsetsWithDup(test_nums))