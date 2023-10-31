# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp ={}

        # return the list of fbt with n nodes
        def backtrack(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            if n in dp:
                return dp[n]
            
            res = []
            for l in range(n): # left sub-tree
                r = n - 1 - l
                leftTrees, rightTrees = backtrack(l), backtrack(r) # will return all possible trees

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))
        
            dp[n] = res
            return res
        
        return backtrack(n)
            