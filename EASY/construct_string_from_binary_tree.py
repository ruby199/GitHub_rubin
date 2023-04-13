# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []

        def preorder(root):
            if not root:
                return

            res.append(str(root.val))

            if root.left or root.right:
                res.append("(")
                preorder(root.left)
                res.append(")")

                if root.right:
                    res.append("(")
                    preorder(root.right)
                    res.append(")")

        preorder(root)

        return "".join(res)
