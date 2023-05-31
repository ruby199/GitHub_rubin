# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # We have at least k elements in the tree
        # In order. - using stack
        n = 0
        stack = []
        cur = root

        while cur and stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop() # most recent element
            n += 1
            if n == k:
                return cur.val
            cur = cur.right # go back up


