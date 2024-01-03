"""
Problem Link: https://leetcode.com/problems/balanced-binary-tree/

[DEF] Height-Balanced: A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

How to Solve:
1. Recursion: Write a helper function that recursively checks each node in the tree. (info: if curent node is balanced, height of the subtree)
2. Height Calculation: For each node, calculate the height of its left & right subtrees. (recursively)
3. Balance Check: current node's left&right balanced? height difference <= 1?
4. Efficiency: Avoid redundant calculations.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        def dfs(node):
            # Base case:
            if not node:
                return True, 0
            
            # Recursively check left & right subtrees
            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            # Check if the current node is balanced
            is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

            # Calculate the height of the current node
            height = max(left_height, right_height) + 1

            return is_balanced, height

        return dfs(root)[0]
            



def buildTree(nodeList):
    if not nodeList:
        return None
    root = TreeNode(nodeList[0])
    nodes = [root]
    idx = 1
    while nodes and idx < len(nodeList):
        node = nodes.pop(0)
        if nodeList[idx] is not None:
            node.left = TreeNode(nodeList[idx])
            nodes.append(node.left)
        idx += 1
        if idx < len(nodeList) and nodeList[idx] is not None:
            node.right = TreeNode(nodeList[idx])
            nodes.append(node.right)
        idx += 1
    return root

def test_isBalanced():
    sol = Solution()
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], True),
        ([1, 2, 2, 3, 3, None, None, 4, 4], False),
        ([], True)
    ]

    for i, (tree, expected) in enumerate(test_cases):
        root = buildTree(tree)
        result = sol.isBalanced(root)
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"

    print("All tests passed!")

test_isBalanced()
