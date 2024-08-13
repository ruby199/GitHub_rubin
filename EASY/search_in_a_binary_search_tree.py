"""
Problem Link: https://leetcode.com/problems/search-in-a-binary-search-tree/description/?envType=study-plan-v2&envId=leetcode-75

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root, val):
        if root is None:
            return None
        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)




def test_solution():
    # Create a sample BST:
    #       4
    #      / \
    #     2   7
    #    / \
    #   1   3

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    solution = Solution()

    # Test case 1: Search for a value that exists
    result = solution.searchBST(root, 2)
    assert result is not None and result.val == 2, "Test case 1 failed"

    # Test case 2: Search for a value that does not exist
    result = solution.searchBST(root, 5)
    assert result is None, "Test case 2 failed"

    print("All test cases passed!")


# Run the test cases
test_solution()