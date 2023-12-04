# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # Base case: If the current node is None, return None
        if not root:
            return None
        
        # If the current node's value is greater than 'high', 
        # trim the right subtree and return the result of trimming the left subtree
        if root.val > high:
            return self.trimBST(root.left, low, high)

        # If the current node's value is less than 'low', 
        # trim the left subtree and return the result of trimming the right subtree
        if root.val < low:
            return self.trimBST(root.right, low, high)

        # Recursively trim the left and right subtrees
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        # Return the root as it lies within the [low, high] range
        return root
