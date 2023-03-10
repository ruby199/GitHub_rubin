# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0] # golbal variable (because we are going to have nested function depth first search passing in only one parameter-the node of the root)

        def depth_first_search(root):
            if not root: # base case: if the root is null
                return -1 
            left = depth_first_search(root.left) # find the height of the left sub tree
            right = depth_first_search(root.right) # find the height of the right sub tree

            # use the left and right height to find the diameter of the current root we are traversing
            # max of it self and our updated diameter
            result[0] = max(result[0], 2 + left + right)

            return 1 + max(left, right)

        depth_first_search(root)
        return result[0]