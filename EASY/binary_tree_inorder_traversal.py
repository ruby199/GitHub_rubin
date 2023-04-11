# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive solution 1
        res = []

        def inorder(root):
            if not root: # root is null
                return
            # inorder Traversal
            inorder(root.left) # pass in the left subtree
            res.append(root.val) # process the root node itself
            inorder(root.right) # do the same algorithm to the right subtree

        inorder(root)

        return res


    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        # iterative solution 2
        res = []
        stack = []
        cur = root
         
        while cur or stack:
            while cur: # real node then go left as long as we can
                stack.append(cur) 
                cur = cur.left # cur down to the left
            cur = stack.pop() 
            res.append(cur.val)
            cur = cur.right
        
        return res
