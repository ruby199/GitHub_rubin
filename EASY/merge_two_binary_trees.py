# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(root1, root2):
        # if they are both empty return null
        if not root1 and not root2:
            return None

        # if null value, we should fill it with 0
        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0

        # create new tree object (merged tree)
        root = TreeNode(v1+v2)

        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return root