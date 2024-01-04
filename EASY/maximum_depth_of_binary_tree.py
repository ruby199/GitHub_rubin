"""
Problem Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

"""

# Definition for a binary tree node
class TreeNode:
    def __iniit__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        # Base case: if the current node is None, the depth is 0
        if root is None:
            return 0

        # Recursively find the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # The depth of the current node is 1 plus the maximum depth of its subtrees
        return max(left_depth, right_depth) + 1
    
# class Solution:
#     def maxDepth(self, root):
#         def dfs(node):
#             # Base case:
#             if not node:
#                 return 0
            
#             left_depth = dfs(node.left)
#             right_depth = dfs(node.right)
#             depth = max(left_depth, right_depth) + 1
#             return depth
#         return dfs(root)