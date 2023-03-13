# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if not root:
            return None
        
        # swap the children
        temp = root.left
        root.left = root.right
        root.right = temp 

        # recurrive function
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# print(Solution.invertTree([4,7,2,9,6,3,1]))
