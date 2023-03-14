# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def mergeTrees(self.root1, self.root2):
        # if they are both empty return null
        if not self.root1 and not self.root2:
            return None

        # if null value, we should fill it with 0
        v1 = self.root1.val if self.root1 else 0
        v2 = self.root2.val if self.root2 else 0

        # create new tree object (merged tree)
        root = TreeNode(v1+v2)

        # Merge both tree
        root.left = self.mergeTrees(self.root1.left if self.root1 else None, self.root2.left if self.root2 else None)
        root.right = self.mergeTrees(self.root1.right if self.root1 else None, self.root2.right if self.root2 else None)

        return root