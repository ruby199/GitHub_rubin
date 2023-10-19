# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # The function checks if two binary trees are flip equivalent.
    # Type optional means they can be either a 'TreeNode' or 'None'
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # If both trees are None, both trees are empty and thus equivalent. Return ture
        if not root1 or not root2:
            return not root1 and not root2
        # If values of the two roots are different, then the trees cannot be flip equivalent. Return False
        if root1.val != root2.val:
            return False
        
        # First, check if the left subtree of root1 is equivalent to the left subtree of root2 AND
        # if the right subtree of root1 is equivalent to the right subtree of root2 (non-flipped case)

        # Then check the flipped case: if the left subtree of root1 is equivalent to the right subtree of root2 AND
        # if right subtree of root1 is equivalent to left subtree of root2
        
        temp = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        return temp or self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)

