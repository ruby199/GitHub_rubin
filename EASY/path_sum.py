# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # use sub function
        def dfs(node, curSum):
            # if empty (meaing there does not exist any root-leaf path even if target sum is 0)
            if not node:
                return False
            
            curSum += node.val # keep tracking
            if not node.left and not node.right: # if leaf node
                return curSum == targetSum # true if leaf node is targetsum, false if not
            
            return (dfs(node.left, curSum) or
                    dfs(node.right, curSum)) # recursive

        return dfs(root, 0)