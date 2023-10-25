# 114. Flatten Binary tree to linked list

"""
Given the root of a binary tree, flatten the tree into a "linked list:

The linked list should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.

The linked list should be in the same order as a pre-order traversal of the binary tree
"""
# Definition for a binary tree:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anythin, modify root in place instead.
        """

        # Define a DFS function to traverse the tree
        def dfs(root):
            if not root:
                return None
            
            # Recursively process the left and right subtrees
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            # If there's a left subtree, adjust pointers to flatten the tree
            if leftTail:
                leftTail.right = root.right 
                root.right = root.left  # Make the left child the new right child
                root.left = None     # Set the left child to None to maintain the structure
            
            # Determine the last node in the modified subtree
            # (either the rightTail, leftTail, or the currrent root)
            last = rightTail or leftTail or root # To where there is children left (root if there are no children)
            return last
        
        # Start the DFS traversal from the root of the tree
        dfs(root)
