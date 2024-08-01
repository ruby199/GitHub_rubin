"""
Problem Link:  https://leetcode.com/problems/path-sum-iii/?envType=study-plan-v2&envId=leetcode-75

[DEF] Prefix Sum: Prefix sum is a sum of the current value with all previous elements starting from the beginning of the structure.

<Prefix Sum: How to Use: Number of ***Continuous*** Subarrays that Sum to Target>


"""

# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, targetSum) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum += node.val
            count = prefix_sums[current_sum - targetSum]
            
            prefix_sums[current_sum] += 1
            
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            
            prefix_sums[current_sum] -= 1
            
            return count

        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        
        return dfs(root, 0)


def test_path_sum():
    # Helper function to create a binary tree from a list
    def create_tree_from_list(values):
        if not values:
            return None
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        while i < len(values):
            current = queue.pop(0)
            if values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1
        return root

    sol = Solution()

    # Test case 1
    root1 = create_tree_from_list([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    targetSum1 = 8
    expected_output1 = 3
    assert sol.pathSum(root1, targetSum1) == expected_output1, f"Test case 1 failed"

    # Test case 2
    root2 = create_tree_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    targetSum2 = 22
    expected_output2 = 3
    assert sol.pathSum(root2, targetSum2) == expected_output2, f"Test case 2 failed"

    print("All test cases passed.")

# Run the tests
test_path_sum()